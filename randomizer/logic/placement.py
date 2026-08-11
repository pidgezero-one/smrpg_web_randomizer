"""Core placement algorithms for randomizer."""
from __future__ import annotations
from typing import TYPE_CHECKING, Callable
import random
from copy import copy

from ..types.prizelocation import FrogDiscipleLocation, StarPieceLocation
from ..types.logic import Inventory
from ..types.prize import StarPiecePrize, CharacterPrize, SpellPrize, KeyPrize
from ..types.flags import KeyItemsAnywhere, SpellsAnywhere, StarPieceAvailability
from randomizer.utils.debug_output import debug_print

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

_AREA_WEIGHT_CAP = 15


def _area_spread_applies(item: Prize, world: GameWorld) -> bool:
    """True for prize types whose eligible pool is opened up by an "anywhere" flag.

    Only these three widen from a handful of dedicated slots to the ~500 standard
    locations, and only then does an area's raw location count start to dominate
    where the prize lands. Every other prize type keeps plain sphere selection.
    """
    if isinstance(item, StarPiecePrize):
        return world.settings.isflag_enabled(StarPieceAvailability)
    if isinstance(item, KeyPrize):
        return world.settings.isflag_enabled(KeyItemsAnywhere)
    if isinstance(item, SpellPrize):
        return world.settings.isflag_enabled(SpellsAnywhere)
    return False


def _select_by_area(
    locations: list[PrizeLocation],
    sphere_map: dict[PrizeLocation, int],
) -> PrizeLocation:
    """Pick a world area first, then a location inside it.

    Grouping is done on `locations`, which the caller has ALREADY filtered down to
    what is accessible, accepting and empty. The cap therefore narrows against live
    availability, never against an area's total roster: an area with 8 of its 10
    locations still open competes with weight min(8, cap), not min(10, cap), and the
    location is then drawn from those 8. Narrowing must not run ahead of
    availability, or the draw could land on an area whose remaining locations were
    already spoken for.
    """
    by_area: dict[object, list[PrizeLocation]] = {}
    for loc in locations:
        by_area.setdefault(getattr(loc, "_world_area", None), []).append(loc)

    if len(by_area) == 1:
        return _select_by_sphere(locations, sphere_map)

    areas = list(by_area)
    weights = [min(len(by_area[area]), _AREA_WEIGHT_CAP) for area in areas]
    chosen_area = random.choices(areas, weights=weights, k=1)[0]
    # Sphere weighting still decides which location within the chosen area.
    return _select_by_sphere(by_area[chosen_area], sphere_map)


def _select_location(
    item: Prize,
    locations: list[PrizeLocation],
    sphere_map: dict[PrizeLocation, int],
    world: GameWorld,
) -> PrizeLocation:
    """Route a placement to area-spread selection or plain sphere selection."""
    if len(locations) == 1:
        return locations[0]
    if _area_spread_applies(item, world):
        return _select_by_area(locations, sphere_map)
    return _select_by_sphere(locations, sphere_map)


def _diagnose_placement_failure(
    world: "GameWorld",
    pending: list["Prize"],
    candidate_locations: list["PrizeLocation"],
) -> None:
    """Print diagnostic info when placement gets stuck (debug mode only)."""
    if not world.settings.debug_mode:
        return

    player_has = collect_accessible_items(world)

    placed: list[str] = []
    for loc in candidate_locations:
        if loc.has_item:
            placed.append(f"  {type(loc).__name__}: {type(loc.prize).__name__}")
    debug_print(f"\n[DEBUG] === PLACEMENT FAILURE ===")
    debug_print(f"[DEBUG] Already placed ({len(placed)} items):")
    for line in placed:
        debug_print(f"[DEBUG] {line}")

    empty_candidates = [l for l in candidate_locations if not l.has_item]
    accessible_empty = [l for l in empty_candidates if l.can_access(player_has, world)]
    debug_print(f"[DEBUG] Empty candidate locations: {len(empty_candidates)}, accessible: {len(accessible_empty)}")
    debug_print(f"[DEBUG] Unplaceable items ({len(pending)}):")
    for item in pending:
        accepting = [l for l in accessible_empty if l.can_accept(item, player_has, world)]
        if accepting:
            debug_print(f"[DEBUG]   {type(item).__name__}: {len(accepting)} locations could accept (bug?)")
        else:
            inaccessible_accepting = [
                l for l in empty_candidates
                if not l.can_access(player_has, world) and l.can_accept(item, Inventory(), world)
            ]
            debug_print(f"[DEBUG]   {type(item).__name__}: 0 accessible accepting locations"
                  f" ({len(inaccessible_accepting)} inaccessible could accept)")


# Bounds for the last-resort stall repair below. They only cap work on a path
# that would otherwise raise, so genuinely unsolvable input still terminates.
_MAX_REPAIR_STALLS = 4
_MAX_REPAIR_VALIDATIONS = 64


def _legal_placements(world: GameWorld) -> set[PrizeLocation]:
    """Placed locations that are currently reachable and legal for their prize.

    Not every filled location qualifies: prizes seeded before place() runs
    (vanilla holds, debug overrides) were never checked against can_accept.
    Snapshotting the set that *is* legal lets the repair below demand "no worse
    than before" instead of "perfect", which a pre-existing violation would
    make unachievable.
    """
    inventory = collect_accessible_items(world)
    legal: set[PrizeLocation] = set()
    for loc in world.locations.values():
        prize = loc.prize
        if prize is None:
            continue
        if loc.can_access(inventory, world) and loc.can_accept(prize, inventory, world):
            legal.add(loc)
    return legal


def _still_legal(
    world: GameWorld,
    baseline: set[PrizeLocation],
    moved: PrizeLocation,
) -> bool:
    """True if every placement in baseline, plus moved, is still legal."""
    inventory = collect_accessible_items(world)
    for loc in (*baseline, moved):
        prize = loc.prize
        if prize is None:
            return False
        if not loc.can_access(inventory, world):
            return False
        if not loc.can_accept(prize, inventory, world):
            return False
    return True


def _repair_stall(
    world: GameWorld,
    pending: list[Prize],
    candidate_locations: list[PrizeLocation],
    on_placed: Callable[[Prize, PrizeLocation], None] | None,
) -> bool:
    """Free one occupied location for a stalled item by relocating its prize.

    Placement is first-fit with no backtracking, so a legal assignment can be
    unreachable purely because an earlier pick took the only location a later
    item could have used. On a stall this tries every (stalled item, occupied
    location, free location) triple and commits the first swap after which
    everything that was legal before is still legal.

    Returns True if an item was placed. Consumes no randomness, and leaves the
    world byte-for-byte untouched when it returns False.
    """
    baseline = _legal_placements(world)
    inventory = collect_accessible_items(world)
    hosts = [l for l in candidate_locations if l.has_item and l in baseline]
    frees = [
        l for l in candidate_locations
        if not l.has_item and l.can_access(inventory, world)
    ]
    if not hosts or not frees:
        return False

    validations = 0
    for item in pending:
        # can_accept() picks and pins a character for a spell, with an RNG roll.
        # Keep the repair clear of both so a failed repair leaves the random
        # stream exactly where it was.
        if isinstance(item, SpellPrize):
            continue
        for host in hosts:
            displaced = host.prize
            if displaced is None or isinstance(displaced, SpellPrize):
                continue
            host.set_prize(None)
            if not host.can_accept(item, inventory, world):
                host.set_prize(displaced)
                continue
            for target in frees:
                if target.has_item:
                    continue
                if not target.can_accept(displaced, inventory, world):
                    continue
                host.set_prize(item)
                target.set_prize(displaced)
                validations += 1
                # host is in baseline, so this also re-checks it holding item.
                if _still_legal(world, baseline, target):
                    pending.remove(item)
                    if on_placed is not None:
                        on_placed(item, host)
                        on_placed(displaced, target)
                    return True
                target.set_prize(None)
                host.set_prize(None)
                if validations >= _MAX_REPAIR_VALIDATIONS:
                    host.set_prize(displaced)
                    return False
            host.set_prize(displaced)
    return False


def _try_repair(
    world: GameWorld,
    pending: list[Prize],
    candidate_locations: list[PrizeLocation],
    on_placed: Callable[[Prize, PrizeLocation], None] | None,
) -> bool:
    """_repair_stall with the random stream pinned across the attempt."""
    state = random.getstate()
    try:
        return _repair_stall(world, pending, candidate_locations, on_placed)
    finally:
        random.setstate(state)


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
    repairs_left = _MAX_REPAIR_STALLS if world.allow_placement_repair else 0
    priority_types = tuple(priority_classes) if priority_classes else ()

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
                    selected = _select_location(
                        chosen, accessible_locations, sphere_map, world
                    )
                    selected.set_prize(chosen)
                    pending.remove(chosen)
                    placements_count += 1
                    if on_placed:
                        on_placed(chosen, selected)
                    continue
            # Fall through to normal placement if no priority item can be placed

        character_items = [item for item in pending if isinstance(item, CharacterPrize)]

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

            if len(accessible_locations) > 0:
                selected = _select_location(
                    character, accessible_locations, sphere_map, world
                )
                selected.set_prize(character)
                pending.remove(character)
                placements_count += 1
                if on_placed:
                    on_placed(character, selected)
                continue  # Go back to the start of the loop

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
            selected = _select_location(item, accessible_locations, sphere_map, world)
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
                if repairs_left > 0:
                    repairs_left -= 1
                    if _try_repair(world, pending, candidate_locations, on_placed):
                        placements_count += 1
                        continue
                _diagnose_placement_failure(world, pending, candidate_locations)
                raise PlacementException(len(pending), [type(p).__name__ for p in pending])
            # Overflow is only safe once every must-fill location is filled.
            # If any candidate location that cannot be empty is still missing a
            # prize, report it as a real placement failure instead of silently
            # dropping pending items.
            unfilled_must_fill = [
                l for l in candidate_locations
                if not l.has_item and not l.can_be_empty(world)
            ]
            if unfilled_must_fill:
                if repairs_left > 0:
                    repairs_left -= 1
                    if _try_repair(world, pending, candidate_locations, on_placed):
                        placements_count += 1
                        continue
                _diagnose_placement_failure(world, pending, candidate_locations)
                raise PlacementException(len(pending), [type(p).__name__ for p in pending])
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

    debug_print("\n" + "=" * 80)
    debug_print("LOCATION DIAGNOSTIC REPORT")
    debug_print("=" * 80)

    for loc in world.locations.values():
        loc_name = type(loc).__name__
        loc_type = type(loc)

        if loc_type in debug_locations:
            prize_name = type(loc.prize).__name__ if loc.prize else "None"
            debug_print(f"{BLUE}[DEBUG] {loc_name}: {prize_name}{RESET}")
            continue

        if not loc.has_item:
            if loc.can_be_empty(world):
                debug_print(f"{GREY}[EMPTY-OK] {loc_name}: no prize (allowed to be empty){RESET}")
            else:
                debug_print(f"{RED}[EMPTY-ERROR] {loc_name}: no prize (NOT allowed to be empty){RESET}")
            continue

        prize_type = type(loc.prize)
        prize_name = prize_type.__name__
        originally_held = loc.originally_held

        if originally_held is not None and isinstance(loc.prize, originally_held):
            debug_print(f"{CYAN}[UNCHANGED] {loc_name}: {prize_name}{RESET}")
        else:
            orig_name = originally_held.__name__ if originally_held else "None"
            debug_print(f"{GREEN}[SHUFFLED] {loc_name}: {orig_name} -> {prize_name}{RESET}")

    debug_print("=" * 80 + "\n")

