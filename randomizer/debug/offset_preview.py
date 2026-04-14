"""Ordered list provider for offset-based prize preview and assignment.

Single source of truth for all ordered lists and offset computations.
Both frontend (via JSON) and backend (at randomization time) use this.
"""

from __future__ import annotations

import inspect

from randomizer.progression.prizelocations import (
    MushrooomWayBossFight,
    MushroomKingdomBossFight,
    BanditsWayBossFight,
    Mimic1BossFight,
    KeroSewersBossFight,
    ForestMazeBossFight,
    OuterMinesBossFight,
    InnerMinesBossFight,
    InnerMinesPostgameBossFight,
    BoosterTowerIndoorBossFight,
    BoosterTowerIndoorBossFightRemake,
    BoosterTowerBalconyBossFight,
    MarrymoreBossFight,
    MarrymoreBossFightRemake,
    SeasideBeachBossFight,
    ShipPasswordBossFight,
    Mimic2BossFight,
    ShipFinalBossFight,
    ShipPostgameBossFight,
    LandsEndCloudBoss,
    TempleBossFight,
    TempleBossFightPostgame,
    DojoFirstFight,
    DojoSecondFight,
    DojoThirdFight,
    DojoFourthFight,
    DojoFifthFight,
    MonstroSealedDoorBossFight,
    MonstroSealedDoorBossFightPostgame,
    Mimic3BossFight,
    BeanValleyPlanterBossFight,
    StatueRoomBossFight,
    GiantEggBossFight,
    NimbusFinalBossFight,
    VolcanoBridgeBossFight,
    VolcanoExitBossFight,
    ObstacleCourseFinalFight,
    KeepAfterObstaclesBossFight,
    KeepChandelierBossFight,
    KeepFinalBossFight,
    FactoryEntranceBossFight,
    FactoryTransitionBossFight,
    InnerFactoryFirstFight,
    InnerFactorySecondFight,
    InnerFactoryThirdFight,
    InnerFactoryFourthFight,
    FinalBossFight,
)
from randomizer.progression import prizelocations as _prizelocations_module
from randomizer.progression.prizes import (
    SlotsPrize1,
    SlotsPrize2,
    SlotsPrize3,
    FirstMimicFightLauncher,
    SecondMimicFightLauncher,
    ThirdMimicFightLauncher,
)
from randomizer.types.prizelocation import (
    TreasureChestLocationRow,
    InvisibleFlagLocation,
)
from randomizer.types.prize import SlotsPrize

# --- Ordered Lists ---

BOSS_LOCATIONS: list[type] = [
    MushrooomWayBossFight,
    MushroomKingdomBossFight,
    BanditsWayBossFight,
    Mimic1BossFight,
    KeroSewersBossFight,
    ForestMazeBossFight,
    OuterMinesBossFight,
    InnerMinesBossFight,
    InnerMinesPostgameBossFight,
    BoosterTowerIndoorBossFight,
    BoosterTowerIndoorBossFightRemake,
    BoosterTowerBalconyBossFight,
    MarrymoreBossFight,
    MarrymoreBossFightRemake,
    SeasideBeachBossFight,
    ShipPasswordBossFight,
    Mimic2BossFight,
    ShipFinalBossFight,
    ShipPostgameBossFight,
    LandsEndCloudBoss,
    TempleBossFight,
    TempleBossFightPostgame,
    DojoFirstFight,
    DojoSecondFight,
    DojoThirdFight,
    DojoFourthFight,
    DojoFifthFight,
    MonstroSealedDoorBossFight,
    MonstroSealedDoorBossFightPostgame,
    Mimic3BossFight,
    BeanValleyPlanterBossFight,
    StatueRoomBossFight,
    GiantEggBossFight,
    NimbusFinalBossFight,
    VolcanoBridgeBossFight,
    VolcanoExitBossFight,
    ObstacleCourseFinalFight,
    KeepAfterObstaclesBossFight,
    KeepChandelierBossFight,
    KeepFinalBossFight,
    FactoryEntranceBossFight,
    FactoryTransitionBossFight,
    InnerFactoryFirstFight,
    InnerFactorySecondFight,
    InnerFactoryThirdFight,
    InnerFactoryFourthFight,
    FinalBossFight,
]

# Derive prize order from locations' vanilla assignments so offset 0 = vanilla.
BOSS_PRIZES: list[type] = [loc._originally_held for loc in BOSS_LOCATIONS]

SLOTS_PRIZES: list[type] = [SlotsPrize1, SlotsPrize2, SlotsPrize3]

MIMIC_PRIZES: list[type] = [
    FirstMimicFightLauncher,
    SecondMimicFightLauncher,
    ThirdMimicFightLauncher,
]


# --- Helper Functions ---


def _get_classes_in_definition_order(base_class: type) -> list[type]:
    """Return subclasses of base_class defined in prizelocations, in source definition order.

    Uses inspect.getsourcelines to sort by the line number where each class is defined,
    rather than alphabetical order (which is what inspect.getmembers returns).
    """
    classes = []
    for _, cls in inspect.getmembers(_prizelocations_module, inspect.isclass):
        if cls is base_class:
            continue
        if not issubclass(cls, base_class):
            continue
        try:
            _, lineno = inspect.getsourcelines(cls)
        except (OSError, TypeError):
            lineno = float("inf")
        classes.append((lineno, cls))

    classes.sort(key=lambda pair: pair[0])
    return [cls for _, cls in classes]


def _get_eligible_chest_rooms() -> list[type]:
    """Return TreasureChestLocationRow subclasses eligible for SlotsPrize.

    Eligible means SlotsPrize is NOT in the class's _blacklist.
    Deduplicated to one per room set (first encountered in definition order wins).
    Classes are returned in source definition order from prizelocations.py.
    """
    seen_room_sets: set[frozenset[int]] = set()
    eligible: list[type] = []

    for cls in _get_classes_in_definition_order(TreasureChestLocationRow):
        blacklist = getattr(cls, "_blacklist", None) or []
        has_slots_blacklist = any(
            issubclass(b, SlotsPrize) if isinstance(b, type) else False
            for b in blacklist
        )
        if has_slots_blacklist:
            continue

        rooms = getattr(cls, "_rooms", None) or []
        room_key = frozenset(rooms)
        if room_key in seen_room_sets:
            continue
        seen_room_sets.add(room_key)
        eligible.append(cls)

    return eligible


def _get_eligible_mimic_chests() -> list[type]:
    """Return TreasureChestLocationRow subclasses eligible for mimic placement.

    All treasure chests are eligible (blacklists are ignored for debug offset mode).
    No room deduplication: chests that share a room with another testable chest
    are still included so the mimic offset slider can target them individually.
    Classes are returned in source definition order from prizelocations.py.
    """
    return _get_classes_in_definition_order(TreasureChestLocationRow)


def _get_invisible_flag_locations() -> list[type]:
    """Return all InvisibleFlagLocation subclasses in definition order from prizelocations.py.

    Classes are returned in source definition order from prizelocations.py.
    """
    return _get_classes_in_definition_order(InvisibleFlagLocation)


def get_ordered_lists() -> dict:
    """Return a dict with ordered lists of class name strings.

    Keys: boss_locations, boss_prizes, eligible_chests, eligible_mimics,
    mimic_prizes, invisible_flags, flag_rooms
    """
    invisible_flags = _get_invisible_flag_locations()
    return {
        "boss_locations": [cls.__name__ for cls in BOSS_LOCATIONS],
        "boss_prizes": [cls.__name__ for cls in BOSS_PRIZES],
        "eligible_chests": [cls.__name__ for cls in _get_eligible_chest_rooms()],
        "eligible_mimics": [cls.__name__ for cls in _get_eligible_mimic_chests()],
        "mimic_prizes": [cls.__name__ for cls in MIMIC_PRIZES],
        "invisible_flags": [cls.__name__ for cls in invisible_flags],
        "flag_rooms": [
            sorted(list(getattr(cls, "_rooms", None) or [])) for cls in invisible_flags
        ],
    }


def compute_offset_assignments(offset: int, mimic_offset: int | None = None) -> dict:
    """Compute offset-based assignments for bosses, slots, mimics, and flags.

    Args:
        offset: The offset value to apply for rotating boss/slot/flag assignments.
        mimic_offset: Independent offset for mimic fight placement. When None
            the main ``offset`` is reused. With ``stride=1`` and the
            undeduplicated chest list, successive values of ``mimic_offset``
            slide each mimic fight through every individual chest (including
            chests that share a room with another testable chest).

    Returns:
        A dict with:
        - bosses: list of (location_name, prize_name) tuples
        - slots: list of 3 (chest_name, slots_prize_name) tuples
        - mimics: list of 3 (chest_name, mimic_prize_name) tuples
        - flags: list of 3 flag_name strings
        - boss_overrides: dict of {location_name: prize_class} for backend
        - slot_overrides: list of (chest_class, slots_prize_class) for backend
        - mimic_overrides: list of (chest_class, mimic_prize_class) for backend
        - flag_classes: list of 3 flag location classes for backend
    """
    if mimic_offset is None:
        mimic_offset = offset
    eligible_chests = _get_eligible_chest_rooms()
    mimic_chests = _get_eligible_mimic_chests()
    invisible_flags = _get_invisible_flag_locations()

    # Boss assignments: location[i] gets prize[(i + offset) % num_prizes]
    num_prizes = len(BOSS_PRIZES)
    boss_assignments = []
    boss_overrides = {}
    for i, location in enumerate(BOSS_LOCATIONS):
        prize = BOSS_PRIZES[(i + offset) % num_prizes]
        boss_assignments.append((location.__name__, prize.__name__))
        boss_overrides[location.__name__] = prize

    # Slots assignments: 3 chests starting at (offset * 3) % len(eligible_chests)
    num_chests = len(eligible_chests)
    slots_start = (offset * 3) % num_chests if num_chests > 0 else 0
    slot_assignments = []
    slot_overrides = []
    for i in range(3):
        chest = eligible_chests[(slots_start + i) % num_chests]
        prize = SLOTS_PRIZES[i]
        slot_assignments.append((chest.__name__, prize.__name__))
        slot_overrides.append((chest, prize))

    # Mimic assignments: 3 consecutive chests starting at mimic_offset,
    # stepping by 1 (not 3) so each individual mimic fight can be dialed
    # into any individual chest via the mimic_offset slider. Chests already
    # used by slots are skipped (a single chest can't hold two prizes).
    slot_classes = {chest_cls for chest_cls, _ in slot_overrides}
    num_mimic_chests = len(mimic_chests)
    mimic_start = mimic_offset % num_mimic_chests if num_mimic_chests > 0 else 0
    mimic_assignments = []
    mimic_overrides = []
    idx = mimic_start
    picked = 0
    while picked < 3 and idx < mimic_start + num_mimic_chests:
        chest = mimic_chests[idx % num_mimic_chests]
        if chest not in slot_classes:
            prize = MIMIC_PRIZES[picked]
            mimic_assignments.append((chest.__name__, prize.__name__))
            mimic_overrides.append((chest, prize))
            picked += 1
        idx += 1

    # Flag assignments: pick 3 flags using a stride of num_flags // 3 starting
    # at index `offset`. This spreads the picks across the list so all flags
    # can be tested within ~num_flags / 3 offsets, and naturally avoids room
    # collisions because the stride exceeds the typical same-room clustering.
    # If a stride pick happens to collide, walk forward until a non-colliding
    # flag is found.
    num_flags = len(invisible_flags)
    flag_assignments = []
    flag_classes = []
    picked_rooms: set[int] = set()
    picked_indices: set[int] = set()
    if num_flags > 0:
        stride = max(1, num_flags // 3)
        for k in range(3):
            base = (offset + k * stride) % num_flags
            for w in range(num_flags):
                idx = (base + w) % num_flags
                if idx in picked_indices:
                    continue
                flag = invisible_flags[idx]
                flag_room_set = set(getattr(flag, "_rooms", None) or [])
                if flag_room_set & picked_rooms:
                    continue
                flag_assignments.append(flag.__name__)
                flag_classes.append(flag)
                picked_rooms |= flag_room_set
                picked_indices.add(idx)
                break

    return {
        "bosses": boss_assignments,
        "slots": slot_assignments,
        "mimics": mimic_assignments,
        "flags": flag_assignments,
        "boss_overrides": boss_overrides,
        "slot_overrides": slot_overrides,
        "mimic_overrides": mimic_overrides,
        "flag_classes": flag_classes,
    }
