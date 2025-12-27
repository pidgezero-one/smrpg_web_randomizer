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
)

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
) -> None:
    """Place items at locations using assumed-reachability algorithm.

    For each item, assumes all other items are collected and finds
    a location where this item can be placed while remaining reachable.

    Args:
        world: The game world containing locations and settings
        items: List of items to place
        locations: List of locations where items can be placed
        can_overflow: If True, allows more items than locations
        on_placed: Optional callback(item, location) called after each placement

    Raises:
        ValueError: If there are more items than locations (when can_overflow=False)
        ValueError: If no valid location can be found for an item
    """
    print("place begins", debug_time())
    from ..types.logic import Inventory as Inv

    remaining_to_fill = Inv(items)

    if not can_overflow and len(remaining_to_fill) > len(
        [l for l in locations if not l.has_item]
    ):
        raise ValueError("Trying to fill more items than available locations")
    
    def attempt_place(item: Prize, fl: list[PrizeLocation], assumed: Inventory) -> bool:
        for l in fl:
            if l.has_item:
                continue
            if not l.can_access(assumed, world):
                continue
            if not l.can_accept(item, assumed, world):
                continue
            l.set_prize(item)
            if on_placed:
                on_placed(item, l)
            print(debug_time(), "placed", type(item), "at", type(l))
            return True
        return False


    # For each required item, place it assuming we can get all other items.
    for item in items:
        # Get items we can get assuming we have everything but the one we're placing.
        remaining_to_fill.remove(item)
        assumed_items = collect(world, remaining_to_fill)

        filtered_locations = locations
        if isinstance(item, KeyPrize):
            filtered_locations = world.extra_key_item_locations
        elif isinstance(item, StarPiecePrize):
            threshold = random.randint(0, 10)
            if threshold < 3:
                filtered_locations = world.star_piece_locations
            else:
                filtered_locations = world.extra_star_piece_locations
        elif isinstance(item, CharacterPrize):
            filtered_locations = world.character_recruitment_locations
        elif isinstance(item, (SlotsPrize, EXPStarPrize, MimicFightInitiatorPrize)):
            filtered_locations = world.chest_locations
        elif isinstance(item, (CoinPrize, FrogCoinPrize)):
            filtered_locations = world.coin_locations
        elif isinstance(item, SpellPrize):
            filtered_locations = world.spell_locations
        elif isinstance(item, BossFightPrize):
            filtered_locations = world.boss_fight_locations
        else:
            filtered_locations = world.standard_locations
        placed = attempt_place(item, filtered_locations, assumed_items)

        if not placed:
            # Debug: show why placement failed
            empty_locs = [l for l in filtered_locations if not l.has_item]
            accessible_locs = [l for l in empty_locs if l.can_access(assumed_items, world)]
            acceptable_locs = [l for l in accessible_locs if l.can_accept(item, assumed_items, world)]
            print(f"FAILED to place {type(item).__name__}:")
            print(f"  filtered_locations: {len(list(filtered_locations))}")
            print(f"  empty: {empty_locs}")
            print(f"  accessible: {accessible_locs}")
            print(f"  acceptable: {acceptable_locs}")
            print(f"  inaccessible:{[l for l in empty_locs if l not in accessible_locs]}")
            print(f"  assumed_items: {assumed_items}")
            print(f"  set: {world.locations.values()}")


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
                empty_locations.remove(loc)
                break