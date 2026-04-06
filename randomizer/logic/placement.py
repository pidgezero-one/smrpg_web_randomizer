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


def compute_location_spheres(world: GameWorld) -> dict[PrizeLocation, int]:
    """Compute the sphere number for each accessible location.

    Sphere 0 = reachable with empty inventory.
    Sphere N+1 = newly reachable after collecting all items from spheres 0..N.
    """
    accessible_items = Inventory()
    seen: set[PrizeLocation] = set()
    sphere_map: dict[PrizeLocation, int] = {}
    sphere = 0

    while True:
        newly_accessible = [
            l for l in world.locations.values()
            if l not in seen and l.can_access(accessible_items, world)
        ]
        if not newly_accessible:
            break

        gained_items = False
        for loc in newly_accessible:
            sphere_map[loc] = sphere
            seen.add(loc)
            if loc.has_item:
                accessible_items.append(loc.prize)
                gained_items = True

        if not gained_items:
            break
        sphere += 1

    return sphere_map


def _select_by_sphere(
    locations: list[PrizeLocation],
    sphere_map: dict[PrizeLocation, int],
) -> PrizeLocation:
    """Select a location with weighted bias toward higher spheres.

    Weight = sphere + 1 (sphere 0 -> weight 1, sphere 1 -> weight 2, etc.)
    """
    if len(locations) == 1:
        return locations[0]
    weights = [sphere_map.get(loc, 0) + 1 for loc in locations]
    return random.choices(locations, weights=weights, k=1)[0]


def _diagnose_placement_failure(
    world: "GameWorld",
    pending: list["Prize"],
    candidate_locations: list["PrizeLocation"],
) -> None:
    """Print diagnostic info when placement gets stuck (debug mode only)."""
    if not world.settings.debug_mode:
        return

    player_has = collect_accessible_items(world)

    # Show what's already placed
    placed: list[str] = []
    for loc in candidate_locations:
        if loc.has_item:
            placed.append(f"  {type(loc).__name__}: {type(loc.prize).__name__}")
    print(f"\n[DEBUG] === PLACEMENT FAILURE ===")
    print(f"[DEBUG] Already placed ({len(placed)} items):")
    for line in placed:
        print(f"[DEBUG] {line}")

    # Show why each pending item is stuck
    empty_candidates = [l for l in candidate_locations if not l.has_item]
    accessible_empty = [l for l in empty_candidates if l.can_access(player_has, world)]
    print(f"[DEBUG] Empty candidate locations: {len(empty_candidates)}, accessible: {len(accessible_empty)}")
    print(f"[DEBUG] Unplaceable items ({len(pending)}):")
    for item in pending:
        accepting = [l for l in accessible_empty if l.can_accept(item, player_has, world)]
        if accepting:
            print(f"[DEBUG]   {type(item).__name__}: {len(accepting)} locations could accept (bug?)")
        else:
            inaccessible_accepting = [
                l for l in empty_candidates
                if not l.can_access(player_has, world) and l.can_accept(item, Inventory(), world)
            ]
            print(f"[DEBUG]   {type(item).__name__}: 0 accessible accepting locations"
                  f" ({len(inaccessible_accepting)} inaccessible could accept)")


def place(
    world: GameWorld,
    to_place: list[Prize],
    can_overflow: bool = False,
    on_placed: Callable[[Prize, PrizeLocation], None] | None = None,
    force_frog_disciple: bool = False,
    location_filter: Callable[[PrizeLocation], bool] | None = None,
    priority_classes: set[type[Prize]] | None = None,
):
    """Place prizes into locations.

    Args:
        world: The game world.
        to_place: List of prizes to place.
        can_overflow: If True, allow placement to finish with unplaced items.
        on_placed: Callback when a prize is placed.
        force_frog_disciple: Prefer FrogDiscipleLocation for placement.
        location_filter: Optional filter - only consider locations where this returns True.
        priority_classes: If provided, every 4th placement will attempt to place
            an item matching one of these types first, to ensure high-unlock-volume
            items are spread throughout the placement order.
    """
    pending = copy(to_place)
    iteration = 0
    placements_count = 0
    priority_types = tuple(priority_classes) if priority_classes else ()

    # Get the set of valid locations (apply filter if provided)
    def get_candidate_locations():
        locs = world.locations.values()
        if location_filter is not None:
            return [l for l in locs if location_filter(l)]
        return list(locs)

    candidate_locations = get_candidate_locations()

    while pending:
        iteration += 1
        length_at_start = len(pending)

        # Compute sphere depths for weighted location selection
        sphere_map = compute_location_spheres(world)

        # Priority detour: every 4th placement, try to place a high-volume item
        if priority_types and (placements_count + 1) % 4 == 0:
            priority_pending = [
                item for item in pending
                if isinstance(item, priority_types)
            ]
            if priority_pending:
                chosen = random.choice(priority_pending)
                player_has = collect_accessible_items(world)
                accessible_locations = [
                    l for l in candidate_locations
                    if l.can_access(player_has, world)
                    and l.can_accept(chosen, player_has, world)
                    and not l.has_item
                ]
                if isinstance(chosen, StarPiecePrize):
                    star_locations = [
                        l for l in accessible_locations
                        if isinstance(l, StarPieceLocation)
                    ]
                    if random.randint(0, 10) < 4 and star_locations:
                        accessible_locations = star_locations
                if accessible_locations:
                    selected = _select_by_sphere(accessible_locations, sphere_map)
                    selected.set_prize(chosen)
                    pending.remove(chosen)
                    placements_count += 1
                    if on_placed:
                        on_placed(chosen, selected)
                    continue
            # Fall through to normal placement if no priority item can be placed

        # Check if there's a character in the pending list
        character_items = [item for item in pending if isinstance(item, CharacterPrize)]

        # If there's a character, try to place it first (prefer gate-critical ones)
        if character_items:
            if priority_types:
                pri = [c for c in character_items if isinstance(c, priority_types)]
                non = [c for c in character_items if not isinstance(c, priority_types)]
                character_items = pri + non
            character = character_items[0]
            player_has = collect_accessible_items(world)
            accessible_locations = [
                l for l in candidate_locations
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
                selected = _select_by_sphere(accessible_locations, sphere_map)
                selected.set_prize(character)
                pending.remove(character)
                placements_count += 1
                if on_placed:
                    on_placed(character, selected)
                continue  # Go back to the start of the loop
            # If character can't be placed yet, fall through to place other items

        # Standard placement algorithm for all items (including character if it couldn't be placed)
        random.shuffle(pending)
        # Try priority items first to prevent non-critical items from consuming
        # limited typed locations (e.g. BossFightLocation) before gate-critical items
        if priority_types:
            pri_items = [item for item in pending if isinstance(item, priority_types)]
            non_items = [item for item in pending if not isinstance(item, priority_types)]
            ordered_pending = pri_items + non_items
        else:
            ordered_pending = pending
        placed_this_iteration = False
        for _, item in enumerate(ordered_pending):
            player_has = collect_accessible_items(world)
            #print(f"  Inventory: {[type(i).__name__ for i in player_has]}")
            accessible_locations = [
                l for l in candidate_locations
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
                if reduce < 4 and star_locations:
                    accessible_locations = star_locations
            if len(accessible_locations) == 0:
                # Move onto the next item to see if it can be placed
                continue
            placed_this_iteration = True
            selected = _select_by_sphere(accessible_locations, sphere_map)
            selected.set_prize(item)
            pending.remove(item)
            placements_count += 1
            if on_placed:
                on_placed(item, selected)
            break
            # Start again from the beginning of the now-shortened pending list

        if len(pending) == 0:
            break
        if len(pending) == length_at_start:
            if not can_overflow:
                _diagnose_placement_failure(world, pending, candidate_locations)
                raise PlacementException(len(pending), [type(p).__name__ for p in pending])
            else:
                break


def diagnose_empty_locations(world: "GameWorld") -> None:
    """Print diagnostic information about all locations with color coding.

    Colors:
    - Grey: received no prize, allowed to be empty
    - Red: received no prize, NOT allowed to be empty (error)
    - Blue: received debug prize
    - Cyan: prize unchanged from original
    - Green: received a prize different from original (shuffled)
    """
    # ANSI color codes
    GREY = "\033[90m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    CYAN = "\033[96m"
    BLUE = "\033[94m"
    RESET = "\033[0m"

    # Get debug locations if they were tracked during shuffle_prizes
    debug_locations: set[type["PrizeLocation"]] = getattr(world, '_debug_locations', set())

    print("\n" + "=" * 80)
    print("LOCATION DIAGNOSTIC REPORT")
    print("=" * 80)

    for loc in world.locations.values():
        loc_name = type(loc).__name__
        loc_type = type(loc)

        # Check if this was a debug override
        if loc_type in debug_locations:
            prize_name = type(loc.prize).__name__ if loc.prize else "None"
            print(f"{BLUE}[DEBUG] {loc_name}: {prize_name}{RESET}")
            continue

        # Check if location has no prize
        if not loc.has_item:
            if loc.can_be_empty(world):
                print(f"{GREY}[EMPTY-OK] {loc_name}: no prize (allowed to be empty){RESET}")
            else:
                print(f"{RED}[EMPTY-ERROR] {loc_name}: no prize (NOT allowed to be empty){RESET}")
            continue

        # Location has a prize - check if it matches original
        prize_type = type(loc.prize)
        prize_name = prize_type.__name__
        originally_held = loc.originally_held

        if originally_held is not None and isinstance(loc.prize, originally_held):
            # Prize is same as original
            print(f"{CYAN}[UNCHANGED] {loc_name}: {prize_name}{RESET}")
        else:
            # Prize was shuffled
            orig_name = originally_held.__name__ if originally_held else "None"
            print(f"{GREEN}[SHUFFLED] {loc_name}: {orig_name} -> {prize_name}{RESET}")

    print("=" * 80 + "\n")

