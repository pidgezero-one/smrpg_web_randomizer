"""Derived lookup tables computed once from world state.

Extracted from types/gameworld.py.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from randomizer.types.prizelocation import (
    BoosterHillLocation,
    NPCLocationRow,
    StandingLocation,
    TreasureChestLocation,
)
from smrpgpatchbuilder.datatypes.levels.classes import (ChestClone, ChestNPC)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import (AreaObject)

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


def _compute_check_bit_mapping(world: GameWorld) -> tuple[
    dict[str, tuple[int, int, bool]],
    dict[int, int],
    dict[int, int],
]:
    """Compute chest state table bit positions for chest check locations.

    The chest state table at BW-RAM $3D80 (FxPak $E03D80) uses cumulative
    bit packing by room ID: room 0 gets its bits first, then room 1, etc.
    Only chest-type objects (ChestNPC and ChestClone) get bits - other object
    types are skipped. Within a room, chests are numbered sequentially.

    Returns:
        (check_mapping, room_bit_offsets, room_chest_counts) where:
        - check_mapping: {location_class_name: (fxpak_addr, bit_index, set_when_checked)}
        - room_bit_offsets: {room_id: cumulative_bit_offset}
        - room_chest_counts: {room_id: chest_object_count}
    """

    FXPAK_BASE = 0xE03D80
    NPC_AREA_OBJECT_START = 0x14  # AreaObject(0x14) = object index 0

    # Cumulative bit offset per room (rooms ordered by ID 0-511).
    # Only ChestNPC and ChestClone objects get bits in this table.
    cumulative = 0
    room_bit_offsets: dict[int, int] = {}
    room_chest_counts: dict[int, int] = {}
    for room_id in range(len(world.rooms._rooms)):
        room_bit_offsets[room_id] = cumulative
        room = world.rooms._rooms[room_id]
        count = (
            sum(1 for obj in room.objects if isinstance(obj, (ChestNPC, ChestClone)))
            if room is not None
            else 0
        )
        room_chest_counts[room_id] = count
        cumulative += count

    # Map TreasureChestLocation checks to bit positions.
    # The bit index within a room is the chest's position among chest-type
    # objects in the room (not its general area object index).
    mapping: dict[str, tuple[int, int, bool]] = {}
    for loc_cls, loc in world.locations.items():
        if not isinstance(loc, TreasureChestLocation):
            continue
        class_name = loc_cls.__name__
        for npc_ao, room_id in zip(loc._npc_ids, loc._rooms):
            ao = npc_ao if isinstance(npc_ao, AreaObject) else AreaObject(npc_ao + NPC_AREA_OBJECT_START)
            obj_idx = int(ao) - NPC_AREA_OBJECT_START
            # Count chest objects before this area object index
            room = world.rooms._rooms[room_id]
            chest_idx = 0
            if room is not None:
                for i, obj in enumerate(room.objects):
                    if i >= obj_idx:
                        break
                    if isinstance(obj, (ChestNPC, ChestClone)):
                        chest_idx += 1
            bit_pos = room_bit_offsets[room_id] + chest_idx
            addr = FXPAK_BASE + (bit_pos // 8)
            bit = bit_pos % 8
            mapping[class_name] = (addr, bit, False)  # cleared = opened
            break  # first room is the primary

    return mapping, room_bit_offsets, room_chest_counts


def _compute_npc_presence_mapping(world: GameWorld) -> dict[str, tuple[int, int, bool]]:
    """Compute NPC presence bit positions for NPC-despawn-based check locations.

    The NPC presence table at BW-RAM $6D20 (FxPak $E02D20) uses cumulative
    bit packing by room ID: room 0 gets bits for ALL its objects first,
    then room 1, etc. A cleared bit (1->0) means the NPC was removed.

    Only maps StandingLocation and NPCLocationRow subclasses that define
    _npc_ids. TreasureChestLocations are skipped (already detected by
    chest bit mapping).

    Returns:
        {location_class_name: (fxpak_addr, bit_index, set_when_checked)}
        where set_when_checked=False (bit CLEAR = check done).
    """

    FXPAK_BASE = 0xE02D20
    NPC_AREA_OBJECT_START = 0x14

    # Cumulative bit offset: count ALL objects per room (not just chests)
    cumulative = 0
    room_bit_offsets: dict[int, int] = {}
    for room_id in range(len(world.rooms._rooms)):
        room_bit_offsets[room_id] = cumulative
        room = world.rooms._rooms[room_id]
        count = len(room.objects) if room is not None else 0
        cumulative += count

    # Map locations that use NPC presence for check detection.
    # Skip TreasureChestLocation (already handled by chest bit mapping).
    # StandingLocation uses _npc_ids; NPCLocationRow uses _check_npc_ids
    # (_npc_ids on NPCLocationRow controls model replacement, not tracking).
    mapping: dict[str, tuple[int, int, bool]] = {}
    for loc_cls, loc in world.locations.items():
        if isinstance(loc, StandingLocation):
            npc_ids = loc._npc_ids
        elif isinstance(loc, NPCLocationRow):
            npc_ids = loc._check_npc_ids
        else:
            continue
        if not npc_ids:
            continue

        class_name = loc_cls.__name__
        for npc_ao, room_id in zip(npc_ids, loc._rooms):
            ao = (
                npc_ao
                if isinstance(npc_ao, AreaObject)
                else AreaObject(npc_ao + NPC_AREA_OBJECT_START)
            )
            obj_idx = int(ao) - NPC_AREA_OBJECT_START
            bit_pos = room_bit_offsets[room_id] + obj_idx
            addr = FXPAK_BASE + (bit_pos // 8)
            bit = bit_pos % 8
            mapping[class_name] = (addr, bit, False)  # bit CLEAR = done
            break  # first room is the primary
    return mapping


def _compute_booster_hill_mapping(world: GameWorld) -> dict[str, int]:
    """Compute Booster Hill flower counter thresholds for check locations.

    BoosterHillLocation checks use the byte counter at BW-RAM $70B1
    (FxPak $E030B1). A check with _70B1_id=N is complete when the
    counter value >= N+1.

    Returns:
        {location_class_name: threshold} where threshold = _70B1_id + 1.
    """
    mapping: dict[str, int] = {}
    for loc_cls, loc in world.locations.items():
        if not isinstance(loc, BoosterHillLocation):
            continue
        mapping[loc_cls.__name__] = loc._70B1_id + 1
    return mapping


__all__ = ['_compute_check_bit_mapping', '_compute_npc_presence_mapping', '_compute_booster_hill_mapping']
