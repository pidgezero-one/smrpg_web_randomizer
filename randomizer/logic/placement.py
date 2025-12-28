"""Core placement algorithms for randomizer."""
from __future__ import annotations
from typing import TYPE_CHECKING, Callable
import random

from .utils import debug_time
from ..types.prize import (
    KeyPrize,
    StarPiecePrize,
    CharacterPrize,
    SlotsPrize,
    EXPStarPrize,
    MimicFightInitiatorPrize,
    CoinPrize,
    FrogCoinPrize,
    SpellPrize,
    BossFightPrize, 
    ItemPrize
)
from ..types.prizelocation import FrogDiscipleLocation

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld
    from ..types.prizelocation import PrizeLocation
    from ..types.prize import Prize
    from ..types.logic import Inventory


def collect(
    world: GameWorld,
    starting_inventory: Inventory | None = None,
) -> Inventory:
    """Collect all items reachable from the starting inventory.

    Uses a fixed-point algorithm to repeatedly find accessible locations
    and add their items until no new items can be found.

    Args:
        world: The game world containing locations and settings
        starting_inventory: Optional starting items (default: empty)

    Returns:
        Inventory containing all reachable items
    """
    from ..types.logic import Inventory as Inv

    my_items = Inv()
    if starting_inventory is not None:
        my_items.extend(starting_inventory)

    available = [l for l in world.locations.values() if l.has_item]

    # Search all locations and collect items until we can't get any more.
    while True:
        search_locations = [
            l for l in available if l.can_access(my_items, world)
        ]
        available = [l for l in available if l not in search_locations]
        found = Inv([l.prize for l in search_locations])  # type: ignore
        my_items.extend(found)
        if len(found) == 0:
            break

    return my_items


def place(
    world: GameWorld,
    items: list[Prize],
    locations: list[PrizeLocation],
    can_overflow: bool = False,
    on_placed: Callable[[Prize, PrizeLocation], None] | None = None,
) -> list[Prize]:
    """Place items at locations using assumed-reachability algorithm with retry.

    For each item, assumes all other items are collected and finds
    a location where this item can be placed while remaining reachable.

    If an item can't be placed (e.g., due to location dependencies), it's
    deferred and retried after other items are placed. This continues until
    either all items are placed or no progress can be made.

    Args:
        world: The game world containing locations and settings
        items: List of items to place
        locations: List of locations where items can be placed
        can_overflow: If True, allows more items than locations
        on_placed: Optional callback(item, location) called after each placement

    Returns:
        List of items that could not be placed (empty if all succeeded)

    Raises:
        ValueError: If there are more items than locations (when can_overflow=False)
    """
    from ..types.logic import Inventory as Inv

    if not can_overflow and len(items) > len(
        [l for l in locations if not l.has_item]
    ):
        raise ValueError("Trying to fill more items than available locations")

    def get_filtered_locations(item: Prize, assumed_items: Inventory) -> list[PrizeLocation]:
        """Get the appropriate location list for an item type."""
        if isinstance(item, KeyPrize):
            return list(world.extra_key_item_locations)
        elif isinstance(item, StarPiecePrize):
            threshold = random.randint(0, 10)
            if threshold < 6:
                return list(world.star_piece_locations)
            else:
                return list(world.extra_star_piece_locations)
        elif isinstance(item, CharacterPrize):
            return list(world.character_recruitment_locations)
        elif isinstance(item, (SlotsPrize, EXPStarPrize, MimicFightInitiatorPrize)):
            return list(world.chest_locations)
        elif isinstance(item, (CoinPrize, FrogCoinPrize)):
            return list(world.coin_locations)
        elif isinstance(item, SpellPrize):
            return list(world.spell_locations)
        elif isinstance(item, BossFightPrize):
            return list(world.boss_fight_locations)
        else:
            frog = random.randint(0, 10)
            if frog < 3:
                for l in world.standard_locations:
                    if isinstance(l, FrogDiscipleLocation) and not l.has_item and l.can_access(assumed_items, world) and l.can_accept(item, assumed_items, world):
                        return [l]
            return list(world.standard_locations)

    def attempt_place(item: Prize, fl: list[PrizeLocation], assumed: Inventory) -> bool:
        """Try to place an item at any valid location."""
        for l in fl:
            if l.has_item:
                continue
            if not l.can_access(assumed, world):
                continue
            if not l.can_accept(item, assumed, world):
                continue
            l.set_prize(item)
            world.notify_prize_placed(l, item)  # Update caches
            if on_placed:
                on_placed(item, l)
            print(debug_time(), "placed", type(item).__name__, "*" if (isinstance(item, ItemPrize) and item._monstro_shuffle) else "", "at", type(l).__name__, "*" if l.monstro_shuffle else "")
            return True
        return False

    # Items waiting to be placed
    pending = list(items)
    random.shuffle(pending)

    # Track items that couldn't be placed in the current pass
    failed_items: list[Prize] = []

    while pending:
        made_progress = False
        deferred: list[Prize] = []

        # Build assumed inventory from all pending items
        remaining_to_fill = Inv(pending)

        for item in pending:
            # Assume we have everything except the item we're placing
            remaining_to_fill.remove(item)
            assumed_items = collect(world, remaining_to_fill)

            filtered_locations = get_filtered_locations(item, assumed_items)
            random.shuffle(filtered_locations)
            placed = attempt_place(item, filtered_locations, assumed_items)

            if placed:
                made_progress = True
            else:
                # Couldn't place - defer for retry
                deferred.append(item)
                # Add back to remaining for next item's assumed inventory
                remaining_to_fill.append(item)

        if not made_progress:
            # No progress in this pass - these items truly can't be placed
            failed_items = deferred
            for item in failed_items:
                print(f"FAILED to place {type(item).__name__}")
            break

        # Retry deferred items in next pass (shuffle for variety)
        pending = deferred
        if pending:
            random.shuffle(pending)
            print(f"Retrying {len(pending)} deferred items...")

    if failed_items:
        print(f"WARNING: {len(failed_items)} items could not be placed")

    return failed_items


def fill_remaining(
    world: GameWorld,
    items: list[Prize],
    locations: list[PrizeLocation],
) -> None:
    """Fill remaining empty locations with items from the pool.

    Unlike place(), this doesn't check reachability - it just fills
    empty locations that can accept the items.

    Args:
        world: The game world containing locations and settings
        items: List of items to place (will be shuffled internally)
        locations: List of locations where items can be placed
    """
    from ..types.logic import Inventory as Inv

    # Shuffle items for randomization
    items_copy = list(items)
    random.shuffle(items_copy)

    empty_locations = [l for l in locations if not l.has_item]
    empty_inv = Inv()  # Empty inventory for can_accept check

    for item in items_copy:
        for loc in empty_locations:
            if loc.can_accept(item, empty_inv, world):
                loc.set_prize(item)
                world.notify_prize_placed(loc, item)  # Update caches
                empty_locations.remove(loc)
                break