"""Core placement algorithms for randomizer."""
from __future__ import annotations
from typing import TYPE_CHECKING, Callable
import random
from copy import copy

from ..types.prizelocation import FrogDiscipleLocation, StarPieceLocation
from ..types.logic import Inventory
from ..types.prize import StarPiecePrize, CharacterPrize

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld
    from ..types.prizelocation import PrizeLocation
    from ..types.prize import Prize


class PlacementException(Exception):
    """Raised when placement fails with unplaced items."""
    def __init__(self, unplaced_count: int, unplaced_items: list):
        self.unplaced_count = unplaced_count
        self.unplaced_items = unplaced_items
        super().__init__(f"No progress made in placement; {unplaced_count} items could not be placed: {unplaced_items}")


def collect_accessible_items(world: GameWorld) -> Inventory:
    progress = True
    accessible_items = Inventory()
    checked = []
    while progress:
        progress = False
        accessible_locations = [
            l for l in world.locations.values()
            if l.can_access(accessible_items, world)
        ]
        for loc in accessible_locations:
            if loc in checked:
                continue
            if loc.has_item:
                accessible_items.append(loc.prize)
                checked.append(loc)
                progress = True
    return accessible_items



def place(
    world: GameWorld,
    to_place: list[Prize],
    can_overflow: bool = False,
    on_placed: Callable[[Prize, PrizeLocation], None] | None = None,
    force_frog_disciple: bool = False,
    debug_label: str | None = None,
):
    pending = copy(to_place)
    iteration = 0

    if debug_label is not None:
        empty_count = sum(1 for l in world.locations.values() if not l.has_item)
        print(f"\n[DEBUG] === Placing pool '{debug_label}' ({len(pending)} items, {empty_count} empty locations) ===")

    while pending:
        iteration += 1
        length_at_start = len(pending)

        # Check if there's a character in the pending list
        character_items = [item for item in pending if isinstance(item, CharacterPrize)]

        # If there's a character, try to place it first
        if character_items:
            character = character_items[0]
            player_has = collect_accessible_items(world)
            accessible_locations = [
                l for l in world.locations.values()
                if l.can_access(player_has, world)
                and l.can_accept(character, player_has, world)
                and not l.has_item
            ]
            if force_frog_disciple:
                frog_locations = [
                    l for l in accessible_locations
                    if isinstance(l, FrogDiscipleLocation)
                ]
                if len(frog_locations) > 0:
                    accessible_locations = frog_locations

            # If the character can be placed, place it
            if len(accessible_locations) > 0:
                random.shuffle(accessible_locations)
                accessible_locations[0].set_prize(character)
                pending.remove(character)
                if on_placed:
                    on_placed(character, accessible_locations[0])
                continue  # Go back to the start of the loop
            # If character can't be placed yet, fall through to place other items

        # Standard placement algorithm for all items (including character if it couldn't be placed)
        random.shuffle(pending)
        placed_this_iteration = False
        for _, item in enumerate(pending):
            player_has = collect_accessible_items(world)
            #print(f"  Inventory: {[type(i).__name__ for i in player_has]}")
            accessible_locations = [
                l for l in world.locations.values()
                if l.can_access(player_has, world)
                and l.can_accept(item, player_has, world)
                and not l.has_item
            ]
            if force_frog_disciple:
                frog_locations = [
                    l for l in accessible_locations
                    if isinstance(l, FrogDiscipleLocation)
                ]
                if len(frog_locations) > 0:
                    accessible_locations = frog_locations
            if isinstance(item, StarPiecePrize):
                star_locations = [
                    l for l in accessible_locations
                    if isinstance(l, StarPieceLocation)
                ]
                reduce = random.randint(0, 10)
                if reduce < 4:
                    accessible_locations = star_locations
            if len(accessible_locations) == 0:
                # Move onto the next item to see if it can be placed
                continue
            placed_this_iteration = True
            random.shuffle(accessible_locations)
            accessible_locations[0].set_prize(item)
            pending.remove(item)
            if on_placed:
                on_placed(item, accessible_locations[0])
            break
            # Start again from the beginning of the now-shortened pending list

        if len(pending) == 0:
            if debug_label is not None:
                print(f"[DEBUG]   Pool '{debug_label}': all {len(to_place)} placed")
            break
        if len(pending) == length_at_start:
            if debug_label is not None:
                unplaced = [type(p).__name__ for p in pending]
                print(f"[DEBUG]   Pool '{debug_label}': STUCK, {len(pending)} unplaced: {unplaced}")
                _diagnose_stuck_items(world, pending)
            if not can_overflow:
                raise PlacementException(len(pending), [type(p).__name__ for p in pending])
            else:
                break


def _log_prize_grants(prize: "Prize") -> str:
    """Debug: Return a comma-separated string of grant types this prize supports."""
    grants = []
    if prize.chest_grant is not None:
        grants.append("chest")
    if prize.npc_grant is not None:
        grants.append("npc")
    if prize.standing_grant is not None:
        grants.append("standing")
    if prize.river_grant is not None:
        grants.append("river")
    if prize.hill_grant is not None:
        grants.append("hill")
    if prize.character_grant is not None:
        grants.append("character")
    if prize.spell_grant is not None:
        grants.append("spell")
    if prize.boss_fight_grant is not None:
        grants.append("boss_fight")
    return ", ".join(grants) if grants else "NONE"


def _get_location_requirements(location: "PrizeLocation") -> str:
    """Debug: Determine what grant type(s) a location requires based on its class hierarchy."""
    from ..types.prizelocation import (
        TreasureChestLocation, StandingLocation, EventLocation,
        RiverLocation, BossFightLocation, BoosterHillLocation,
        CharacterRecruitmentLocation, SpellSlotLocation,
        FrogDiscipleLocation, TreasureShopLocation, KeyItemLocation,
    )

    reqs = []
    if isinstance(location, BoosterHillLocation):
        reqs.append("hill_grant")
    if isinstance(location, StandingLocation):
        reqs.append("standing_grant")
    if isinstance(location, TreasureChestLocation):
        reqs.append("chest_grant")
    if isinstance(location, EventLocation):
        reqs.append("npc_grant")
    if isinstance(location, RiverLocation):
        reqs.append("river_grant")
    if isinstance(location, BossFightLocation):
        reqs.append("boss_fight_grant")
    if isinstance(location, CharacterRecruitmentLocation):
        reqs.append("character_grant")
    if isinstance(location, SpellSlotLocation):
        reqs.append("spell_grant")
    if isinstance(location, FrogDiscipleLocation):
        reqs.append("frog_disciple")
    if isinstance(location, TreasureShopLocation):
        reqs.append("nickname")
    if isinstance(location, KeyItemLocation):
        reqs.append("key_item")
    return ", ".join(reqs) if reqs else "base_only"


def _diagnose_stuck_items(world: "GameWorld", pending: list["Prize"]) -> None:
    """Debug: When placement gets stuck, diagnose why each remaining item can't be placed."""
    player_has = collect_accessible_items(world)
    all_empty = [l for l in world.locations.values() if not l.has_item]
    all_accessible_empty = [l for l in all_empty if l.can_access(player_has, world)]

    print(f"[DEBUG]     ({len(all_empty)} empty, {len(all_accessible_empty)} accessible)")
    for item in pending:
        grants = _log_prize_grants(item)
        accepting = [l for l in all_accessible_empty if l.can_accept(item, player_has, world)]
        if accepting:
            print(f"[DEBUG]     {type(item).__name__} [grants: {grants}]: {len(accepting)} locations could accept (bug?)")
        else:
            # Show what types of empty accessible locations exist
            reject_types: dict[str, int] = {}
            for loc in all_accessible_empty:
                reject_types.setdefault(_get_location_requirements(loc), 0)
                reject_types[_get_location_requirements(loc)] += 1
            print(f"[DEBUG]     {type(item).__name__} [grants: {grants}]: 0 accepting locations")
            for reqs, count in sorted(reject_types.items(), key=lambda x: -x[1])[:5]:
                print(f"[DEBUG]       {count}x locations needing [{reqs}]")


def diagnose_empty_locations(world: "GameWorld") -> None:
    """Debug: Post-placement analysis of why locations are empty."""
    player_has = collect_accessible_items(world)

    all_locs = list(world.locations.values())
    empty_with_orig = [l for l in all_locs if not l.has_item and l.originally_held is not None]
    empty_cant_be = [l for l in empty_with_orig if not l.can_be_empty(world)]

    if not empty_cant_be:
        print(f"\n[DEBUG] Post-placement: no problematic empty locations.")
        return

    print(f"\n{'='*80}")
    print(f"[DEBUG] EMPTY LOCATIONS THAT SHOULD NOT BE EMPTY: {len(empty_cant_be)}")
    print(f"{'='*80}")

    for loc in empty_cant_be:
        accessible = loc.can_access(player_has, world)
        reqs = _get_location_requirements(loc)
        orig_name = loc.originally_held.__name__ if loc.originally_held else "None"

        # Test if the location would accept its own original prize
        orig_accepts = False
        orig_grants = ""
        if loc.originally_held is not None:
            orig_prize = loc.originally_held()
            orig_grants = _log_prize_grants(orig_prize)
            orig_accepts = loc.can_accept(orig_prize, player_has, world)

        print(f"  {type(loc).__name__}")
        print(f"    orig={orig_name}, accessible={accessible}, needs=[{reqs}]")
        print(f"    orig_prize grants=[{orig_grants}], can_accept_orig={orig_accepts}")
        print(f"    MRO: {' → '.join(c.__name__ for c in type(loc).__mro__[:5])}")

