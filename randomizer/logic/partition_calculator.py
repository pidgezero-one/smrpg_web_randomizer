"""Partition calculator for SMRPG rooms.

This module calculates optimal VRAM partition configurations for rooms
based on their NPC contents, chest items, and sprite requirements.

The partition system controls how NPC sprites are loaded into VRAM.
Key components:
- ally_sprite_buffer_size: Space needed for player character sprites (0-3)
- allow_extra_sprite_buffer: Whether packet sprites can be created
- extra_sprite_buffer_size: Number of packet sprites expected (0-15)
- buffers: Three Buffer slots, each with type/space/index settings
- full_palette_buffer: (typically True)

Buffer types:
- THREE_SPRITES_PER_ROW: For format >= 2 gridplane sprites
- FOUR_SPRITES_PER_ROW: For format <= 1 gridplane sprites
- TREASURE_CHEST: For chest sprite (sprite 94)
- COINS: For coin sprites
- EMPTY_*: No specific sprite requirements
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from dataclasses import dataclass, field

from ..data.variables.sprite_names import *
from ..data.variables.room_names import *

from smrpgpatchbuilder.datatypes.levels.classes import (
    Buffer,
    BufferSpace,
    BufferType,
    ChestNPC,
    Clone,
    Partition,
    VramStore,
)
from ..types.ally import SpriteAnimationState
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    NPC_0,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import AreaObject

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld
    from smrpgpatchbuilder.datatypes.levels.classes import RoomObject
    from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite


# =============================================================================
# Vanilla room state tracking for change detection
# =============================================================================


@dataclass
class VanillaNPCState:
    """Stores vanilla state of an NPC for change detection."""

    sprite_id: int
    is_gridplane: bool
    gridplane_format: (
        int | None
    )  # 0-1 = 4 sprites/row, 2-3 = 3 sprites/row, None = non-gridplane
    is_coin: bool  # True if sprite is a coin (regular, small, frog, small frog)


@dataclass
class VanillaChestState:
    """Stores vanilla state of a chest for change detection."""

    had_coins: bool
    had_exp_star: bool
    had_slots: bool


@dataclass
class VanillaRoomState:
    """Stores vanilla state of a room for change detection."""

    npcs: list[VanillaNPCState]
    chests: list[VanillaChestState]


def snapshot_vanilla_room_states(world: GameWorld) -> None:
    """Capture vanilla NPC sprite states for all rooms with partitions.

    Must be called AFTER update_partition_by_protagonist but BEFORE any
    NPC model shuffling (.render() calls). Stores result on
    world._vanilla_room_states for later change detection.
    """
    states: dict[int, VanillaRoomState] = {}

    for room_id, room in enumerate(world.rooms._rooms):
        if room is None or room.partition is None:
            continue

        npc_states: list[VanillaNPCState] = []
        for obj in room.objects:
            if isinstance(obj, Clone):
                continue
            sprite_id = obj._npc.sprite_id
            is_gridplane, gridplane_format = _get_npc_gridplane_info(world, sprite_id)
            is_coin = sprite_id in COIN_SPRITE_IDS
            npc_states.append(VanillaNPCState(
                sprite_id=sprite_id,
                is_gridplane=is_gridplane,
                gridplane_format=gridplane_format,
                is_coin=is_coin,
            ))

        chest_states: list[VanillaChestState] = []
        states[room_id] = VanillaRoomState(npcs=npc_states, chests=chest_states)

    world._vanilla_room_states = states


@dataclass
class AnimationVramOverride:
    """Declarative animation-based min_vram override for NPC objects.

    Before partition recalculation, if the boss placed at location_class
    has the named animation, compute min_vram from its sequence and set it
    on the room NPC.
    """
    location_class: type    # e.g., InnerMinesBossFight
    room_id: int            # room where NPC appears
    npc_id: AreaObject      # which NPC in the room
    animation_attr: str     # attribute name on boss.animations, e.g. "mines_punch"


def _get_animation_vram_overrides() -> list[AnimationVramOverride]:
    """Build the animation VRAM override registry.

    Imports are deferred to avoid circular dependencies with prizelocation modules.
    """
    from ..progression.prizelocations import InnerMinesBossFight

    return [
        AnimationVramOverride(
            location_class=InnerMinesBossFight,
            room_id=R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE,
            npc_id=NPC_0,
            animation_attr="mines_punch",
        ),
    ]


def _apply_animation_vram_overrides(world: GameWorld, changed_rooms: set[int]) -> None:
    """Apply animation-based min_vram overrides to NPCs in changed rooms.

    For each override whose room is in the changed set, look up the boss
    model's animation sequence and compute the min_vram requirement.
    Must run BEFORE partition recalculation.
    """
    from ..utils.npcs import min_vram_from_sequence_for_sprite
    from ..types.prize import BossFightPrize

    overrides = _get_animation_vram_overrides()

    for override in overrides:
        if override.room_id not in changed_rooms:
            continue

        location = world.locations.get(override.location_class)
        if location is None:
            continue

        assert isinstance(location.prize, BossFightPrize)
        npc_model = location.prize.get_npc_for_slot(world, 4096)
        boss = npc_model()

        if boss.animations is None:
            continue
        animation = getattr(boss.animations, override.animation_attr, None)
        if animation is None:
            continue

        sequence_id = animation.sequence_id
        sprite_id = boss.base.sprite_id
        min_vram = min_vram_from_sequence_for_sprite(world, sprite_id, sequence_id)

        room = world.rooms._rooms[override.room_id]
        assert room is not None
        npc_obj = room.get_npc_by_target_id(override.npc_id)
        npc_obj.set_min_vram_size(min_vram)


def _detect_changed_rooms(world: GameWorld) -> set[int]:
    """Compare current NPC sprite IDs against vanilla snapshot.

    Returns set of room IDs where at least one NPC's sprite_id differs
    from the snapshot taken before shuffling.
    """
    assert world._vanilla_room_states is not None, (
        "snapshot_vanilla_room_states() must be called before change detection"
    )

    changed: set[int] = set()
    for room_id, vanilla_state in world._vanilla_room_states.items():
        room = world.rooms._rooms[room_id]
        if room is None:
            continue

        # Enumerate current non-Clone NPCs
        current_sprites: list[int] = []
        for obj in room.objects:
            if isinstance(obj, Clone):
                continue
            current_sprites.append(obj._npc.sprite_id)

        # Compare against snapshot
        if len(current_sprites) != len(vanilla_state.npcs):
            # NPC count changed (e.g., dummies added) — mark as changed
            changed.add(room_id)
            continue

        for current_sprite_id, vanilla_npc in zip(current_sprites, vanilla_state.npcs):
            if current_sprite_id != vanilla_npc.sprite_id:
                changed.add(room_id)
                break

    return changed


def _recalculate_room_partition(world: GameWorld, room_id: int) -> None:
    """Recompute buffer layout and cannot_clone for a room after NPC shuffling.

    Looks at the current NPC makeup, determines optimal buffer assignments
    based on sprite frequency, sets cannot_clone accordingly, and preserves
    non-clone-buffer partition settings (ally buffer, extra sprite buffer,
    full palette). Carries over main_buffer_space and index_in_main_buffer
    from the original partition, tracked by NPC slot association.

    Algorithm:
    1. Analyze all NPCs: sprite ID, gridplane format
    2. Map original buffers to the NPC indices they served
    3. Group sprites by ID, count frequency, determine buffer needs
    4. Assign up to 3 buffer slots (CHEST→0, COINS→2, gridplane by frequency)
    5. Order gridplane buffers to match NPC object order
    6. Set cannot_clone: False for buffered NPCs, True for all others
    7. Carry over main_buffer_space and index_in_main_buffer from original
       buffers, tracked by NPC slot (not by buffer index or type)
    """
    room = world.rooms._rooms[room_id]
    assert room is not None
    assert room.partition is not None

    existing = room.partition

    # =========================================================================
    # Step 1: Analyze current NPCs
    # =========================================================================
    @dataclass
    class NPCInfo:
        obj_index: int
        sprite_id: int
        is_gridplane: bool
        gridplane_format: int | None  # 0-1 = FOUR, 2-3 = THREE
        is_chest: bool
        is_coin: bool
        force_cannot_clone: bool  # Room-level override — orchestrator must respect

    npc_infos: list[NPCInfo] = []
    for i, obj in enumerate(room.objects):
        if isinstance(obj, Clone):
            continue
        sprite_id = obj._npc.sprite_id
        is_gridplane, fmt = _get_npc_gridplane_info(world, sprite_id)
        is_chest = isinstance(obj, ChestNPC) or sprite_id == CHEST_SPRITE_ID
        is_coin = sprite_id in COIN_SPRITE_IDS
        # Room-level cannot_clone=True is a signal to always use dedicated VRAM
        # (e.g., NPCs with non-gridplane animation sequences despite gridplane mold 0)
        force_cc = obj.cannot_clone is True
        npc_infos.append(NPCInfo(
            obj_index=i,
            sprite_id=sprite_id,
            is_gridplane=is_gridplane,
            gridplane_format=fmt,
            is_chest=is_chest,
            is_coin=is_coin,
            force_cannot_clone=force_cc,
        ))

    # =========================================================================
    # Step 2: Map original buffers → NPC indices they served
    # =========================================================================
    # For carryover of main_buffer_space and index_in_main_buffer.
    # We need the vanilla snapshot to know which NPCs were in which buffers.
    assert world._vanilla_room_states is not None
    vanilla_state = world._vanilla_room_states.get(room_id)

    # original_buffer_settings[buffer_index] = (main_buffer_space, index_in_main_buffer)
    original_buffer_settings: list[tuple[BufferSpace, bool]] = [
        (buf.main_buffer_space, buf.index_in_main_buffer)
        for buf in existing.buffers
    ]

    # Map: obj_index → original buffer index (for carryover tracking)
    obj_to_original_buffer: dict[int, int] = {}
    if vanilla_state is not None:
        # Build type → buffer indices map from original partition
        type_to_indices: dict[BufferType, list[int]] = {}
        for i, buf in enumerate(existing.buffers):
            btype = buf.buffer_type
            if btype not in type_to_indices:
                type_to_indices[btype] = []
            type_to_indices[btype].append(i)

        obj_idx = 0
        vanilla_npc_idx = 0
        while obj_idx < len(room.objects) and vanilla_npc_idx < len(vanilla_state.npcs):
            obj = room.objects[obj_idx]
            if isinstance(obj, Clone):
                obj_idx += 1
                continue
            vanilla_npc = vanilla_state.npcs[vanilla_npc_idx]

            if vanilla_npc.is_gridplane:
                if vanilla_npc.gridplane_format in (0, 1):
                    needed = BufferType.FOUR_SPRITES_PER_ROW
                elif vanilla_npc.gridplane_format in (2, 3):
                    needed = BufferType.THREE_SPRITES_PER_ROW
                else:
                    needed = None
            elif vanilla_npc.is_coin:
                needed = BufferType.COINS
            elif vanilla_npc.sprite_id == CHEST_SPRITE_ID:
                needed = BufferType.TREASURE_CHEST
            else:
                needed = None

            if needed is not None and needed in type_to_indices:
                indices = type_to_indices[needed]
                if indices:
                    obj_to_original_buffer[obj_idx] = indices[0]

            obj_idx += 1
            vanilla_npc_idx += 1

    # =========================================================================
    # Step 3: Determine buffer needs — one buffer per unique sprite ID
    # =========================================================================
    # At runtime, each unique sprite ID gets its own VRAM allocation via
    # the sprite table at $9C4A. Different sprites with the same format
    # do NOT share a buffer — each needs its own slot.
    has_chest = any(n.is_chest for n in npc_infos)
    has_coin = any(n.is_coin for n in npc_infos)

    # Build sprite groups: sprite_id → (buffer_type, npc_count, first_obj_index)
    from collections import Counter
    sprite_to_type: dict[int, BufferType] = {}  # sprite_id → needed buffer type
    sprite_counts: Counter[int] = Counter()
    sprite_first_appearance: dict[int, int] = {}  # sprite_id → first obj_index
    for npc in npc_infos:
        if npc.force_cannot_clone or npc.is_chest or npc.is_coin or not npc.is_gridplane:
            continue
        if npc.gridplane_format in (0, 1):
            sprite_to_type[npc.sprite_id] = BufferType.FOUR_SPRITES_PER_ROW
        elif npc.gridplane_format in (2, 3):
            sprite_to_type[npc.sprite_id] = BufferType.THREE_SPRITES_PER_ROW
        else:
            continue
        sprite_counts[npc.sprite_id] += 1
        if npc.sprite_id not in sprite_first_appearance:
            sprite_first_appearance[npc.sprite_id] = npc.obj_index

    # Count available buffer slots (after reserving for chest/coin)
    available_slots = 3
    if has_chest:
        available_slots -= 1
    if has_coin:
        available_slots -= 1

    # Rank unique sprite IDs by NPC count (most frequent first)
    # Each unique sprite needs its own buffer slot
    ranked_sprites = sorted(
        sprite_to_type.keys(),
        key=lambda sid: sprite_counts[sid],
        reverse=True,
    )

    # Select which sprite IDs get buffer slots (up to available_slots)
    buffered_sprite_ids: set[int] = set()
    # Each selected sprite claims one buffer slot
    selected_buffers: list[tuple[int, BufferType]] = []  # (sprite_id, buffer_type)
    for sprite_id in ranked_sprites:
        if len(selected_buffers) >= available_slots:
            break
        selected_buffers.append((sprite_id, sprite_to_type[sprite_id]))
        buffered_sprite_ids.add(sprite_id)

    # =========================================================================
    # Step 4: Order buffers respecting NPC object order
    # =========================================================================
    # Buffers must appear in the order their first NPC appears in the
    # object list, because the game assigns NPCs to buffers sequentially.
    selected_buffers.sort(
        key=lambda sb: sprite_first_appearance.get(sb[0], 999),
    )

    # Build the 3-slot buffer assignment
    new_buffer_types: list[BufferType] = [BufferType.EMPTY_3] * 3

    if has_chest:
        new_buffer_types[0] = BufferType.TREASURE_CHEST
    if has_coin:
        new_buffer_types[2] = BufferType.COINS

    # Fill remaining slots with ordered sprite buffers
    buffer_queue = list(selected_buffers)
    # Track which sprite_id is in which new buffer index
    sprite_to_new_buffer: dict[int, int] = {}
    for i in range(3):
        if new_buffer_types[i] != BufferType.EMPTY_3:
            continue  # Already assigned (chest or coin)
        if buffer_queue:
            sprite_id, btype = buffer_queue.pop(0)
            new_buffer_types[i] = btype
            sprite_to_new_buffer[sprite_id] = i

    # =========================================================================
    # Step 5: Carry over main_buffer_space and index_in_main_buffer
    # =========================================================================
    # For each new buffer slot, check if any of its NPCs had an original
    # buffer with non-default settings. Carry those forward.
    new_buffer_space: list[BufferSpace] = [BufferSpace.BYTES_0] * 3
    new_index_in_main: list[bool] = [True] * 3  # Default is True

    for i, btype in enumerate(new_buffer_types):
        if btype in (BufferType.TREASURE_CHEST, BufferType.COINS, BufferType.EMPTY_3):
            # For chest/coin/empty, check if original had same type and carry over
            for orig_i, orig_buf in enumerate(existing.buffers):
                if orig_buf.buffer_type == btype:
                    space, index_flag = original_buffer_settings[orig_i]
                    if space.value > new_buffer_space[i].value:
                        new_buffer_space[i] = space
                    new_index_in_main[i] = index_flag
                    break
        else:
            # Gridplane buffer — find NPCs whose sprite_id is assigned to this slot
            for npc in npc_infos:
                if npc.sprite_id not in buffered_sprite_ids:
                    continue
                if sprite_to_new_buffer.get(npc.sprite_id) != i:
                    continue
                # This NPC uses the new buffer. Check its original buffer settings.
                orig_buf_idx = obj_to_original_buffer.get(npc.obj_index)
                if orig_buf_idx is not None:
                    space, index_flag = original_buffer_settings[orig_buf_idx]
                    if space.value > new_buffer_space[i].value:
                        new_buffer_space[i] = space
                    # Carry index_in_main_buffer from original (use first match)
                    if new_index_in_main[i] is True and index_flag is not True:
                        new_index_in_main[i] = index_flag

    # =========================================================================
    # Step 6: Apply buffer changes to the existing partition
    # =========================================================================
    for i in range(3):
        existing.buffers[i].set_buffer_type(new_buffer_types[i])
        existing.buffers[i].set_main_buffer_space(new_buffer_space[i])
        existing.buffers[i].set_index_in_main_buffer(new_index_in_main[i])

    # =========================================================================
    # Step 7: Set cannot_clone on all NPCs
    # =========================================================================
    for npc in npc_infos:
        obj = room.objects[npc.obj_index]
        if npc.force_cannot_clone:
            # Room-level override — always dedicated VRAM, don't touch
            pass
        elif npc.is_chest or npc.is_coin:
            obj.set_cannot_clone(False)
        elif npc.sprite_id in buffered_sprite_ids:
            obj.set_cannot_clone(False)
        else:
            obj.set_cannot_clone(True)

    # =========================================================================
    # Step 8: Log warnings
    # =========================================================================
    # Check for sprites that needed a buffer but didn't get one
    for npc in npc_infos:
        if npc.force_cannot_clone:
            continue  # Intentionally excluded from buffers
        if npc.is_gridplane and npc.sprite_id not in buffered_sprite_ids and not npc.is_chest and not npc.is_coin:
            print(
                f"[PARTITION WARN] Room {room_id}: NPC {npc.obj_index} "
                f"(sprite {npc.sprite_id}, format {npc.gridplane_format}) "
                f"has no matching buffer, set to cannot_clone=True"
            )


def _log_slot_machine_support(world: GameWorld) -> None:
    """Log can_room_support_slots results for all rooms with chests.

    For rooms with slot machine dummy NPCs (last 5 objects with EMPTY_NPC_3
    sprite ID), temporarily swaps them to EMPTY_NPC before checking.
    Debug output only — does not modify any state.
    """
    from ..data.rooms.npcs import EMPTY_NPC

    slot_dummy_sprite_id = SPR1023_EMPTY

    for room_id, room in enumerate(world.rooms._rooms):
        if room is None or room.partition is None:
            continue

        # Check if room has chests
        has_chest = False
        for obj in room.objects:
            if isinstance(obj, Clone):
                continue
            if isinstance(obj, ChestNPC) or obj._npc.sprite_id == CHEST_SPRITE_ID:
                has_chest = True
                break

        if not has_chest:
            continue

        # Check if last 5 objects are slot dummies (all have EMPTY sprite)
        objects = room.objects
        has_dummies = (
            len(objects) >= 5
            and all(
                objects[len(objects) - 5 + j]._npc.sprite_id == slot_dummy_sprite_id
                for j in range(5)
            )
        )

        saved_npcs = []
        if has_dummies:
            # Temporarily swap dummy NPCs to EMPTY_NPC
            for j in range(5):
                idx = len(objects) - 5 + j
                saved_npcs.append(objects[idx]._npc)
                objects[idx]._npc = EMPTY_NPC

        try:
            # Use the room's existing partition parameters for accurate capacity check
            existing = room.partition
            analyze_kwargs = dict(
                max_packets=existing.extra_sprite_buffer_size,
                allow_extra_sprite_buffer=existing.allow_extra_sprite_buffer,
                water=not existing.full_palette_buffer,
            )
            result = can_room_support_slots(world, room_id, **analyze_kwargs)
            analysis = analyze_partition(world, room_id, **analyze_kwargs)
            print(
                f"[SLOT CHECK] Room {room_id}: support={result}"
                f" bitmap_remaining={analysis.bitmap_slots_remaining}"
                f" vram_remaining={analysis.vram_remaining}"
            )
        finally:
            # Restore original dummy NPCs
            if has_dummies:
                for j in range(5):
                    idx = len(objects) - 5 + j
                    objects[idx]._npc = saved_npcs[j]


def update_changed_room_partitions(world: GameWorld) -> None:
    """Recalculate partitions for rooms where NPC models changed.

    Replaces update_shuffed_boss_partitions. Call order:
    1. Detect changed rooms via snapshot diff
    2. Apply animation VRAM overrides (min_vram_size pre-pass)
    3. Recalculate partition for each changed room
    4. Log slot machine support for all chest rooms
    """
    changed_rooms = _detect_changed_rooms(world)
    print(f"[PARTITION] Orchestrator: {len(changed_rooms)} rooms changed")

    # Pre-pass: animation VRAM overrides
    _apply_animation_vram_overrides(world, changed_rooms)

    # Recalculate partitions
    for room_id in sorted(changed_rooms):
        _recalculate_room_partition(world, room_id)

    # Final pass: slot machine support check (all chest rooms, not just changed)
    _log_slot_machine_support(world)


# =============================================================================
# Mapping from extra sprite action states to animation states needed for VRAM
# Used to determine which ally animation states are needed for each room action
# =============================================================================

EXTRA_ACTION_TO_ANIMATION_STATE: dict[
    SpriteAnimationState, list[SpriteAnimationState]
] = {
    # Direct matches (already in _sprites_primary, just need to load themselves)
    SpriteAnimationState.DEFEND: [SpriteAnimationState.DEFEND],
    SpriteAnimationState.SALUTE: [SpriteAnimationState.SALUTE],
    SpriteAnimationState.CHALLENGE: [SpriteAnimationState.CHALLENGE],
    SpriteAnimationState.SLEEP: [SpriteAnimationState.SLEEPING],
    # Surprise/shock animations
    SpriteAnimationState.SURPRISE_FRAME: [
        SpriteAnimationState.SHOCKED_LOOP,
        SpriteAnimationState.SHOCKED_SHADOW,
    ],
    SpriteAnimationState.SURPRISE_FRAME_BACK: [
        SpriteAnimationState.SHOCKED_LOOP_BACKWARDS,
        SpriteAnimationState.SHOCKED_SHADOW_BACKWARDS,
        SpriteAnimationState.SHOCKED_BACKWARDS_SEQUENCE,
    ],
    # Standing/leaning animations
    SpriteAnimationState.STANDING_SLEEP: [SpriteAnimationState.SLEEPING],
    SpriteAnimationState.LEAN_BACK: [SpriteAnimationState.LOOKING_DOWN],
    SpriteAnimationState.LEAN_BACK_2: [SpriteAnimationState.LOOKING_DOWN_AWAY],
    SpriteAnimationState.LEAN_FORWARD: [SpriteAnimationState.LOOKING_DOWN_STATIC],
    # Displeased animations
    SpriteAnimationState.DISPLEASED_FRONT: [SpriteAnimationState.DISPLEASED],
    SpriteAnimationState.DISPLEASED_BACK: [SpriteAnimationState.DISPLEASED],
    # Praise/joy animations
    SpriteAnimationState.PRAISE_FRONT: [
        SpriteAnimationState.JOY,
        SpriteAnimationState.JOY_JUMP,
    ],
    SpriteAnimationState.PRAISE_BACK: [SpriteAnimationState.JOY_BEHIND],
    # Tumble/hurt animations
    SpriteAnimationState.TUMBLE_FRONT: [
        SpriteAnimationState.FLOORED,
        SpriteAnimationState.HURT,
    ],
    SpriteAnimationState.TUMBLE_BACK: [
        SpriteAnimationState.FLOORED,
        SpriteAnimationState.HURT,
    ],
    SpriteAnimationState.RECOIL: [SpriteAnimationState.HURT],
    SpriteAnimationState.FLOP: [SpriteAnimationState.FLOORED],
    SpriteAnimationState.DIZZY: [SpriteAnimationState.SHAKING_HEAD],
    SpriteAnimationState.WOBBLE: [SpriteAnimationState.SHAKING_HEAD],
    # Looking animations
    SpriteAnimationState.LOOK_AT_DOLL: [
        SpriteAnimationState.LOOK_TO_SIDE,
        SpriteAnimationState.LOOK_TO_DOWN,
    ],
    SpriteAnimationState.EXOR: [SpriteAnimationState.LOOK_WAY_UP],
    # Challenge variants
    SpriteAnimationState.CHALLENGE_NIMBUS: [SpriteAnimationState.CHALLENGE],
    # Special animations - map to base states as fallback
    SpriteAnimationState.SWIM: [SpriteAnimationState.SOUTH],
    SpriteAnimationState.WHIRL: [SpriteAnimationState.SOUTH],
    SpriteAnimationState.DOWN_PIPE: [SpriteAnimationState.SOUTH],
    SpriteAnimationState.CROUCH: [SpriteAnimationState.LOOKING_DOWN_STATIC],
    SpriteAnimationState.YOSHI: [SpriteAnimationState.SOUTH],
    SpriteAnimationState.CLIMB: [SpriteAnimationState.FACE_NORTH],
    SpriteAnimationState.CLIMB_FRAME: [SpriteAnimationState.FACE_NORTH],
    SpriteAnimationState.BLACKJACK: [SpriteAnimationState.SOUTH],
    SpriteAnimationState.HOLD_STAR: [SpriteAnimationState.VICTORY_POSE],
    SpriteAnimationState.MUTE: [SpriteAnimationState.SHAKING_HEAD],
}

# Default animation states to always consider (basic movement)
DEFAULT_ANIMATION_STATES = [
    SpriteAnimationState.SOUTH,
    SpriteAnimationState.FACE_NORTH,
    SpriteAnimationState.FACE_SOUTH,
]


def list_unique(arr: list) -> list:
    """Return list with duplicates removed while preserving order."""
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


# Priority order for buffer type assignment
PARTITION_PRIORITY = [
    BufferType.TREASURE_CHEST,
    BufferType.COINS,
    BufferType.EMPTY_3,
    BufferType.FOUR_SPRITES_PER_ROW,
    BufferType.THREE_SPRITES_PER_ROW,
]

# Rooms that need special handling
SPECIAL_CASE_ROOMS = [
    R037_BOOSTER_TOWER_4F_3LEVEL_ROOM_WJUMPING_SPOOKUMS,
    R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER,
    R070_MIDAS_RIVER_1ST_TUNNEL,
    R071_MIDAS_RIVER_2ND_TUNNEL_BOTH_LEFT_AND_RIGHT,
    R072_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT,
    R073_MIDAS_RIVER_4TH_TUNNEL_ON_VERY_BOTTOM_RIGHT,
    R079_ROSE_WAY_MAIN_AREA,
    R205_MUSHROOM_WAY_AREA_03,
    R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09,
    R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
    R233_FOREST_MAZE_AREA_03_UNDERGROUND,
    R236_FOREST_MAZE_AREA_07_UNDERGROUND_WSLEEPING_WIGGLER,
    R463_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1B_BARRELCOUNTING,
    R466_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1C_WORD_PROBLEM,
    R477_BOWSERS_KEEP_2ND_TIME_AREA_02,
]
# 205 - complicated spiney sequence
# 463, 466 - barrel count room and logic problem room need this for some reason

ALWAYS_REQUIRES_COIN_BUFFER = [
    R071_MIDAS_RIVER_2ND_TUNNEL_BOTH_LEFT_AND_RIGHT,
    R072_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT,
    R073_MIDAS_RIVER_4TH_TUNNEL_ON_VERY_BOTTOM_RIGHT,
]

# Rooms that always need triple empty + extra sprite buffer size 1
TRIPLE_EMPTY_EX1_ROOMS = [
    R376_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2B_1ST_FIGHT_CHEWY,
    R377_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2C_1ST_FIGHT_SPARKY,
    R459_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1A_1ST_FIGHT_TERRA_COTTA,
    R460_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1B_1ST_FIGHT_ALLEY_RAT,
    R461_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_1C_1ST_FIGHT_BOBOMB,
    R462_BOWSERS_KEEP_6DOOR_BATTLE_ROOM_2A_1ST_FIGHT_GU_GOOMBA,
    R202_BOOSTER_TOWER_ENTRANCE,
]

# Rooms that always need triple empty + extra sprite buffer size 0
TRIPLE_EMPTY_EX0_ROOMS = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]

# Rooms where chests are close enough together that extra_sprite_buffer_size needs to be 2+
# (player can open multiple chests before packet sprites despawn)
CLOSE_CHEST_ROOMS = {
    R234_FOREST_MAZE_SECRET: 2,  # Forest Maze Secret - 5 floating chests in tight cluster
    R453_BOWSERS_KEEP_AREA_05_DARK_TUNNEL_AFTER_THRONE_ROOM: 2,  # Bowser's Keep - chests close together
}


def _get_complete_sprite(world: GameWorld, sprite_id: int) -> CompleteSprite | None:
    """Get CompleteSprite object for a given sprite ID.

    Uses world.get_sprite() pattern from physical_objects.py which provides
    direct access to animation properties via sprite.animation.properties.
    """
    try:
        return world.get_sprite(sprite_id)
    except (IndexError, AssertionError):
        return None


def _get_npc_gridplane_info(
    world: GameWorld, sprite_id: int
) -> tuple[bool, int | None]:
    """Get gridplane information for an NPC sprite.

    Returns:
        (is_gridplane, format) where format is 0-3 for gridplanes, None for non-gridplanes
    """
    complete_sprite = _get_complete_sprite(world, sprite_id)
    if complete_sprite is None:
        return (False, None)

    molds = complete_sprite.animation.properties.molds
    if not molds or len(molds) == 0:
        return (False, None)

    mold = molds[0]
    if not mold.gridplane:
        return (False, None)

    if not mold.tiles or len(mold.tiles) == 0:
        return (True, None)

    tile = mold.tiles[0]
    tile_format = tile.format  # type: ignore[attr-defined]
    return (True, tile_format)


# =============================================================================
# Ally Buffer Calculation
# Determines VRAM needed for player character based on room's extra_sprite_actions
# =============================================================================


# =============================================================================
# General-purpose partition analysis tool
# =============================================================================

# Coin sprite IDs that require a COINS buffer
COIN_SPRITE_IDS = frozenset({
    SPR0192_COIN,
    SPR0193_SMALL_COIN,
    SPR0194_FROG_COIN,
    SPR0211_SMALL_FROG_COIN,
})

CHEST_SPRITE_ID = SPR0094_TREASURE_CHEST


@dataclass
class NPCAnalysis:
    """Analysis of a single NPC's VRAM requirements."""

    index: int
    sprite_id: int
    vram_store: VramStore
    min_vram: int
    max_sequence_vram: int
    cannot_clone: bool
    is_chest: bool
    is_coin: bool
    is_gridplane: bool
    gridplane_format: int | None
    buffer_type: BufferType
    clone_count: int
    force_cannot_clone: bool
    bitmap_slots: int              # Extra sprite bitmap slots consumed by this parent NPC


# VramStore → number of direction sequences loaded → bitmap slots consumed per parent NPC.
# From ASM trace: each direction sequence takes 1 slot from the extra sprite bitmap at $01B2.
VRAM_STORE_BITMAP_SLOTS: dict[VramStore, int] = {
    VramStore.DIR0_SWSE_NWNE: 2,        # 2 sequences (seq 0, 1)
    VramStore.DIR1_SWSE_NWNE_S: 3,      # 3 sequences (seq 0, 1, 10)
    VramStore.DIR2_SWSE: 1,             # 1 sequence (seq 0)
    VramStore.DIR3_SWSE_NWNE: 2,        # 2 sequences
    VramStore.DIR4_ALL_DIRECTIONS: 5,    # 5 sequences (seq 0, 1, 10, 11, 12)
    VramStore.DIR5_UNKNOWN: 5,           # Same as DIR4 in traced routines
    VramStore.DIR6_UNKNOWN: 5,           # Same as DIR4 in traced routines
    VramStore.DIR7_ALL_DIRECTIONS: 10,   # Up to 10 sequences (player chars only)
}


@dataclass
class BufferAssignment:
    """Assignment of NPCs to a partition buffer slot."""

    buffer_type: BufferType
    buffer_space: BufferSpace
    npc_indices: list[int] = field(default_factory=list)


@dataclass
class PartitionAnalysis:
    """Complete partition analysis for a room."""

    room_id: int
    npcs: list[NPCAnalysis]
    ally_buffer_size: int
    allow_extra_sprite_buffer: bool
    extra_buffer_size: int
    buffers: list[BufferAssignment]
    full_palette: bool
    warnings: list[str] = field(default_factory=list)

    def to_partition(self) -> Partition:
        """Convert this analysis to a Partition object."""
        partition = Partition()
        partition.set_ally_sprite_buffer_size(self.ally_buffer_size)
        partition.set_allow_extra_sprite_buffer(self.allow_extra_sprite_buffer)
        partition.set_extra_sprite_buffer_size(self.extra_buffer_size)

        buffers = []
        for assignment in self.buffers:
            buf = Buffer()
            buf.set_buffer_type(assignment.buffer_type)
            buf.set_main_buffer_space(assignment.buffer_space)
            buffers.append(buf)
        partition.set_buffers(buffers)
        return partition

    def format_report(self) -> str:
        """Format a human-readable analysis report."""
        lines = [f"=== Room {self.room_id} Partition Analysis ==="]
        lines.append(f"Ally buffer size: {self.ally_buffer_size}")
        lines.append(
            f"Extra sprite buffer: {'yes' if self.allow_extra_sprite_buffer else 'no'}"
            + (f" (size={self.extra_buffer_size})" if self.allow_extra_sprite_buffer else "")
        )
        lines.append(f"Full palette: {self.full_palette}")

        for i, assignment in enumerate(self.buffers):
            slot = chr(ord("A") + i)
            space_bytes = assignment.buffer_space * 256
            npcs_str = (
                ", ".join(str(idx) for idx in assignment.npc_indices)
                if assignment.npc_indices
                else "none"
            )
            lines.append(
                f"Buffer {slot}: {assignment.buffer_type.name}"
                + (f" ({space_bytes} bytes)" if space_bytes > 0 else "")
                + f"  NPCs: [{npcs_str}]"
            )

        lines.append(f"VRAM: cursor={self.vram_cursor}, remaining={self.vram_remaining}")
        lines.append(f"Bitmap slots: {self.bitmap_slots_used}/{self.bitmap_slots_capacity} (remaining={self.bitmap_slots_remaining})")

        if self.npcs:
            lines.append("")
            lines.append("NPC Details:")
            for npc in self.npcs:
                flags = []
                if npc.cannot_clone:
                    flags.append("no-clone")
                if npc.is_chest:
                    flags.append("chest")
                if npc.is_coin:
                    flags.append("coin")
                fmt_str = (
                    f"fmt={npc.gridplane_format}"
                    if npc.gridplane_format is not None
                    else "non-gp"
                )
                flags_str = f" [{', '.join(flags)}]" if flags else ""
                lines.append(
                    f"  [{npc.index}] sprite={npc.sprite_id}"
                    f" vram={npc.vram_store.name}"
                    f" min_vram={npc.min_vram}"
                    f" {fmt_str}"
                    f" clones={npc.clone_count}"
                    f" → {npc.buffer_type.name}"
                    f"{flags_str}"
                )

        if self.warnings:
            lines.append("")
            lines.append("Warnings:")
            for warning in self.warnings:
                lines.append(f"  ! {warning}")

        return "\n".join(lines)

    @property
    def bitmap_slots_capacity(self) -> int:
        """Total extra sprite bitmap slots available: (extra_buffer_size + 1) * 4."""
        return (self.extra_buffer_size + 1) * 4

    @property
    def bitmap_slots_used(self) -> int:
        """Total extra sprite bitmap slots consumed by all parent NPCs."""
        return sum(npc.bitmap_slots for npc in self.npcs)

    @property
    def bitmap_slots_remaining(self) -> int:
        """Extra sprite bitmap slots available for additional NPCs."""
        return self.bitmap_slots_capacity - self.bitmap_slots_used

    @property
    def vram_cursor(self) -> int:
        """Total VRAM rows consumed by this partition."""
        cursor = self.ally_buffer_size * 4
        cursor += self.extra_buffer_size
        for buf in self.buffers:
            cursor += buf.buffer_space
        for npc in self.npcs:
            if npc.force_cannot_clone:
                cursor += npc.max_sequence_vram
        return cursor

    @property
    def vram_remaining(self) -> int:
        """VRAM rows available for additional NPCs (32 - vram_cursor)."""
        return 32 - self.vram_cursor


def _analyze_npc(
    world: GameWorld, npc_obj: RoomObject, index: int, clone_count: int = 0
) -> NPCAnalysis:
    """Analyze a single NPC's VRAM requirements.

    Args:
        world: The GameWorld instance.
        npc_obj: The room object (must NOT be a Clone).
        index: The NPC's index in the room's objects list.
        clone_count: Number of Clone objects following this NPC in the objects list.
    """
    npc = npc_obj._npc
    sprite_id = npc.sprite_id

    # Room-level overrides take precedence over NPC-level defaults
    vram_store = npc_obj.directions if npc_obj.directions is not None else npc.directions
    min_vram = npc_obj.min_vram_size if npc_obj.min_vram_size is not None else npc.min_vram_size
    cannot_clone = npc_obj.cannot_clone if npc_obj.cannot_clone is not None else npc.cannot_clone

    # Detect by sprite ID, not just class — a RegularNPC with sprite 94
    # still needs TREASURE_CHEST buffer type for VRAM layout purposes.
    is_chest = isinstance(npc_obj, ChestNPC) or sprite_id == CHEST_SPRITE_ID
    is_coin = sprite_id in COIN_SPRITE_IDS

    is_gridplane, gridplane_format = _get_npc_gridplane_info(world, sprite_id)

    if is_chest:
        buffer_type = BufferType.TREASURE_CHEST
    elif is_coin:
        buffer_type = BufferType.COINS
    elif is_gridplane:
        if gridplane_format in (0, 1):
            buffer_type = BufferType.FOUR_SPRITES_PER_ROW
        elif gridplane_format in (2, 3):
            buffer_type = BufferType.THREE_SPRITES_PER_ROW
        else:
            buffer_type = BufferType.EMPTY_3
    else:
        buffer_type = BufferType.EMPTY_3

    force_cannot_clone = not is_gridplane and not is_chest and not is_coin

    return NPCAnalysis(
        index=index,
        sprite_id=sprite_id,
        vram_store=vram_store,
        min_vram=min_vram,
        max_sequence_vram=0,
        cannot_clone=cannot_clone,
        is_chest=is_chest,
        is_coin=is_coin,
        is_gridplane=is_gridplane,
        gridplane_format=gridplane_format,
        buffer_type=buffer_type,
        clone_count=clone_count,
        force_cannot_clone=force_cannot_clone,
        bitmap_slots=VRAM_STORE_BITMAP_SLOTS.get(vram_store, 1),
    )


def _calculate_buffer_space(npcs: list[NPCAnalysis]) -> BufferSpace:
    """Calculate the BufferSpace needed for a group of NPCs."""
    if not npcs:
        return BufferSpace.BYTES_0
    max_vram = max(npc.min_vram for npc in npcs)
    max_vram = min(max_vram, 7)
    return BufferSpace(max_vram)


def _assign_buffers(
    npc_analyses: list[NPCAnalysis],
    room_id: int,
) -> tuple[list[BufferAssignment], list[str]]:
    """Assign NPCs to 3 buffer slots based on their requirements.

    Rules:
    - TREASURE_CHEST can only go in buffer A (index 0)
    - COINS can only go in buffer C (index 2)
    - Clonable gridplane NPCs fill remaining slots
    - cannot_clone NPCs get dedicated VRAM (not assigned to buffers)
    """
    warnings: list[str] = []

    # Separate NPCs by type.
    # Clonable NPCs determine primary buffer slot assignments.
    # cannot_clone NPCs get dedicated VRAM but still influence the
    # fill strategy for remaining empty slots (compatible format needed).
    chest_npcs = [n for n in npc_analyses if n.is_chest and not n.cannot_clone]
    coin_npcs = [n for n in npc_analyses if n.is_coin and not n.cannot_clone]
    four_spr_npcs = [
        n
        for n in npc_analyses
        if n.buffer_type == BufferType.FOUR_SPRITES_PER_ROW and not n.cannot_clone
    ]
    three_spr_npcs = [
        n
        for n in npc_analyses
        if n.buffer_type == BufferType.THREE_SPRITES_PER_ROW and not n.cannot_clone
    ]
    empty_npcs = [
        n
        for n in npc_analyses
        if n.buffer_type == BufferType.EMPTY_3
        and not n.cannot_clone
        and not n.is_chest
        and not n.is_coin
    ]
    dedicated_npcs = [n for n in npc_analyses if n.cannot_clone]

    # Track gridplane types from ALL NPCs (including cannot_clone)
    # for the fill strategy — these NPCs need compatible buffer format
    all_four_spr = [
        n for n in npc_analyses
        if n.buffer_type == BufferType.FOUR_SPRITES_PER_ROW
    ]
    all_three_spr = [
        n for n in npc_analyses
        if n.buffer_type == BufferType.THREE_SPRITES_PER_ROW
    ]

    # Force coin buffer for Midas River rooms
    force_coins = room_id in [
        R071_MIDAS_RIVER_2ND_TUNNEL_BOTH_LEFT_AND_RIGHT,
        R072_MIDAS_RIVER_3RD_TUNNEL_ON_LEFT,
        R073_MIDAS_RIVER_4TH_TUNNEL_ON_VERY_BOTTOM_RIGHT,
    ]

    # Start with 3 empty buffer slots
    assignments: list[BufferAssignment] = [
        BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
        BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
        BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
    ]

    # Assign TREASURE_CHEST to buffer A if needed
    if chest_npcs:
        assignments[0] = BufferAssignment(
            BufferType.TREASURE_CHEST,
            _calculate_buffer_space(chest_npcs),
            [n.index for n in chest_npcs],
        )

    # Assign COINS to buffer C if needed
    if coin_npcs or force_coins:
        assignments[2] = BufferAssignment(
            BufferType.COINS,
            _calculate_buffer_space(coin_npcs),
            [n.index for n in coin_npcs],
        )

    # Assign gridplane NPCs to remaining open slots.
    # Vanilla fills ALL remaining empty slots with the dominant gridplane type,
    # so multiple NPCs can be loaded simultaneously.
    gridplane_groups = []
    if four_spr_npcs:
        gridplane_groups.append(
            (BufferType.FOUR_SPRITES_PER_ROW, four_spr_npcs)
        )
    if three_spr_npcs:
        gridplane_groups.append(
            (BufferType.THREE_SPRITES_PER_ROW, three_spr_npcs)
        )

    # Sort by count descending so the dominant type gets placed first
    gridplane_groups.sort(key=lambda g: len(g[1]), reverse=True)

    for buf_type, npcs in gridplane_groups:
        # Place into first available empty slot
        placed = False
        for i in range(3):
            if assignments[i].buffer_type == BufferType.EMPTY_3:
                assignments[i] = BufferAssignment(
                    buf_type,
                    _calculate_buffer_space(npcs),
                    [n.index for n in npcs],
                )
                placed = True
                break
        if not placed:
            # Try to merge into an existing matching buffer
            for i in range(3):
                if assignments[i].buffer_type == buf_type:
                    assignments[i].npc_indices.extend(n.index for n in npcs)
                    merged_npcs = [
                        na
                        for na in npc_analyses
                        if na.index in assignments[i].npc_indices
                    ]
                    assignments[i].buffer_space = _calculate_buffer_space(merged_npcs)
                    placed = True
                    break
            if not placed:
                warnings.append(
                    f"No buffer slot available for {buf_type.name} NPCs "
                    f"(indices: {[n.index for n in npcs]})"
                )

    # Fill remaining empty slots with the dominant gridplane type.
    # Use ALL NPCs (including cannot_clone) for type determination,
    # since these NPCs need compatible buffer format in the room.
    all_gp_groups = []
    if all_four_spr:
        all_gp_groups.append(
            (BufferType.FOUR_SPRITES_PER_ROW, all_four_spr)
        )
    if all_three_spr:
        all_gp_groups.append(
            (BufferType.THREE_SPRITES_PER_ROW, all_three_spr)
        )
    all_gp_groups.sort(key=lambda g: len(g[1]), reverse=True)

    if all_gp_groups:
        dominant_type = all_gp_groups[0][0]
        # Use clonable NPCs only for space calculation
        clonable_of_type = [
            n for n in gridplane_groups[0][1]
        ] if gridplane_groups and gridplane_groups[0][0] == dominant_type else []
        space = _calculate_buffer_space(clonable_of_type) if clonable_of_type else BufferSpace.BYTES_0
        for i in range(3):
            if assignments[i].buffer_type == BufferType.EMPTY_3:
                assignments[i] = BufferAssignment(dominant_type, space)

    # Assign non-gridplane clonable NPCs to any available EMPTY_3 slot
    if empty_npcs:
        for i in range(3):
            if assignments[i].buffer_type == BufferType.EMPTY_3:
                assignments[i].npc_indices.extend(n.index for n in empty_npcs)
                assignments[i].buffer_space = _calculate_buffer_space(empty_npcs)
                break

    if dedicated_npcs:
        for npc in dedicated_npcs:
            warnings.append(
                f"NPC [{npc.index}] sprite={npc.sprite_id}: cannot_clone, needs dedicated VRAM"
            )

    return assignments, warnings


def _assign_buffers_v2(
    npc_analyses: list[NPCAnalysis],
    room_id: int,
) -> tuple[list[BufferAssignment], list[str]]:
    """Assign NPCs to 3 buffer slots with strict format matching.

    Rules:
    - TREASURE_CHEST -> buffer A (index 0) if any chests present
    - COINS -> buffer C (index 2) if any animated coins present
    - Format 0-1 gridplane NPCs -> FOUR_SPRITES_PER_ROW buffer
    - Format 2-3 gridplane NPCs -> THREE_SPRITES_PER_ROW buffer
    - Non-gridplane NPCs already have force_cannot_clone=True (from _analyze_npc)
    - If both gridplane formats exist but only one buffer slot remains,
      majority format gets the slot, minority format NPCs get force_cannot_clone=True
    - No hardcoded room-specific logic (caller handles special cases like Midas River)
    - Remaining empty slots filled with EMPTY_3
    """
    warnings: list[str] = []

    # Separate NPCs into groups (only considering assignable NPCs)
    chest_npcs = [n for n in npc_analyses if n.is_chest and not n.force_cannot_clone]
    coin_npcs = [n for n in npc_analyses if n.is_coin and not n.force_cannot_clone]
    four_npcs = [
        n
        for n in npc_analyses
        if n.buffer_type == BufferType.FOUR_SPRITES_PER_ROW and not n.force_cannot_clone
    ]
    three_npcs = [
        n
        for n in npc_analyses
        if n.buffer_type == BufferType.THREE_SPRITES_PER_ROW and not n.force_cannot_clone
    ]

    # Start with 3 empty buffer slots
    assignments: list[BufferAssignment] = [
        BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
        BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
        BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
    ]

    # Assign TREASURE_CHEST to buffer A (index 0) if needed
    if chest_npcs:
        assignments[0] = BufferAssignment(
            BufferType.TREASURE_CHEST,
            BufferSpace.BYTES_0,
            [n.index for n in chest_npcs],
        )

    # Assign COINS to buffer C (index 2) if needed
    if coin_npcs:
        assignments[2] = BufferAssignment(
            BufferType.COINS,
            BufferSpace.BYTES_0,
            [n.index for n in coin_npcs],
        )

    # Collect gridplane groups sorted by count descending (majority first)
    gridplane_groups = []
    if four_npcs:
        gridplane_groups.append(
            (BufferType.FOUR_SPRITES_PER_ROW, four_npcs)
        )
    if three_npcs:
        gridplane_groups.append(
            (BufferType.THREE_SPRITES_PER_ROW, three_npcs)
        )
    gridplane_groups.sort(key=lambda g: len(g[1]), reverse=True)

    # Assign each gridplane group to the first available empty slot
    for buf_type, npcs in gridplane_groups:
        placed = False
        for i in range(3):
            if assignments[i].buffer_type == BufferType.EMPTY_3:
                assignments[i] = BufferAssignment(
                    buf_type,
                    BufferSpace.BYTES_0,
                    [n.index for n in npcs],
                )
                placed = True
                break
        if not placed:
            # No empty slot available — force all NPCs in this group to cannot_clone
            for npc in npcs:
                npc.force_cannot_clone = True
            warnings.append(
                f"Room {room_id}: No buffer slot for {buf_type.name} NPCs "
                f"(indices: {[n.index for n in npcs]}), forced cannot_clone"
            )

    return assignments, warnings


# Protagonist name to CharacterPrize class mapping
_PROTAGONIST_PRIZES: dict[str, type] = {}  # Populated lazily to avoid circular imports


def _get_protagonist_prizes() -> dict[str, type]:
    """Lazily load protagonist name → CharacterPrize mapping."""
    if not _PROTAGONIST_PRIZES:
        from ..progression.prizes import (
            MarioRecruitmentPrize,
            MallowRecruitmentPrize,
            GenoRecruitmentPrize,
            BowserRecruitmentPrize,
            ToadstoolRecruitmentPrize,
        )
        _PROTAGONIST_PRIZES.update({
            "mario": MarioRecruitmentPrize,
            "mallow": MallowRecruitmentPrize,
            "geno": GenoRecruitmentPrize,
            "bowser": BowserRecruitmentPrize,
            "peach": ToadstoolRecruitmentPrize,
            "toadstool": ToadstoolRecruitmentPrize,
        })
    return _PROTAGONIST_PRIZES


def _calculate_ally_buffer_size(
    world: GameWorld,
    room,
    protagonist: str | None,
) -> int:
    """Calculate ally buffer size based on protagonist and room's extra_sprite_actions.

    Args:
        world: GameWorld instance (needed for sprite lookups).
        room: Room instance (needed for extra_sprite_actions).
        protagonist: Character name ("mario", "peach", "bowser", "geno", "mallow")
            or None for default (size 1).

    Returns:
        Ally buffer size (1-3). Returns 1 if protagonist is None or no
        extra sprite actions require larger buffer.
    """
    from ..types.room import Room

    if protagonist is None:
        return 1

    prizes = _get_protagonist_prizes()
    prize_cls = prizes.get(protagonist.lower())
    if prize_cls is None:
        return 1

    character_model = prize_cls().character_model
    if character_model is None:
        return 1

    if not isinstance(room, Room) or not room.extra_sprite_actions:
        return 1

    vram_values: list[int] = []

    # Check default animation states
    for state in DEFAULT_ANIMATION_STATES:
        sprites_dict = character_model.ally._sprites_primary
        if state in sprites_dict:
            prop_id, offset, is_mold = sprites_dict[state]
            if is_mold:
                try:
                    v = character_model._npc.min_vram_from_mold(world, prop_id, offset)
                    vram_values.append(v)
                except (IndexError, AssertionError):
                    pass
            else:
                try:
                    v = character_model._npc.min_vram_from_sequence(world, prop_id, offset)
                    vram_values.append(v)
                except (IndexError, AssertionError):
                    pass

    # Check room's extra_sprite_actions
    for action in room.extra_sprite_actions:
        anim_states = EXTRA_ACTION_TO_ANIMATION_STATE.get(action, [])
        for state in anim_states:
            sprites_dict = character_model.ally._sprites_primary
            if state in sprites_dict:
                prop_id, offset, is_mold = sprites_dict[state]
                if is_mold:
                    try:
                        v = character_model._npc.min_vram_from_mold(world, prop_id, offset)
                        vram_values.append(v)
                    except (IndexError, AssertionError):
                        pass
                else:
                    try:
                        v = character_model._npc.min_vram_from_sequence(world, prop_id, offset)
                        vram_values.append(v)
                    except (IndexError, AssertionError):
                        pass

    if not vram_values:
        return 1
    return min(max(vram_values) + 1, 3)


def analyze_partition(
    world: GameWorld,
    room_id: int,
    *,
    protagonist: str | None = None,
    max_packets: int = 0,
    allow_extra_sprite_buffer: bool | None = None,
    water: bool = False,
    npc_sequence_overrides: dict[int, list[int]] | None = None,
) -> PartitionAnalysis:
    """Analyze a room and compute optimal partition configuration.

    Pure computation — no side effects. Deterministic for identical inputs.

    Args:
        world: GameWorld with loaded sprite data.
        room_id: Room index to analyze.
        protagonist: Character name ("mario", "peach", "bowser", "geno", "mallow")
            for ally buffer sizing. Default None uses ally_buffer_size=1.
        max_packets: Maximum packet sprites active simultaneously. Sets
            extra_sprite_buffer_size directly (1 packet = 1 cursor row).
        allow_extra_sprite_buffer: Whether packet sprites can be created.
            Defaults to True when max_packets > 0, False otherwise.
        water: If True, sets full_palette_buffer=False. Default False.
        npc_sequence_overrides: Per-NPC sequence IDs the NPC will use.
            {npc_object_index: [sequence_id, ...]}. Used to compute buffer
            space from non-gridplane molds in those sequences.

    Returns:
        PartitionAnalysis with computed partition, buffer assignments, and
        force_cannot_clone recommendations.
    """
    room = world.rooms._rooms[room_id]
    assert room is not None, f"Room {room_id} not found"

    if allow_extra_sprite_buffer is None:
        allow_extra_sprite_buffer = max_packets > 0

    # --- Step 1: Enumerate NPCs ---
    objects = room.objects
    npc_analyses: list[NPCAnalysis] = []
    i = 0
    while i < len(objects):
        obj = objects[i]
        if isinstance(obj, Clone):
            i += 1
            continue

        # Count consecutive Clone objects following this NPC
        clone_count = 0
        j = i + 1
        while j < len(objects) and isinstance(objects[j], Clone):
            clone_count += 1
            j += 1

        npc_analysis = _analyze_npc(world, obj, i, clone_count)

        # Apply sequence overrides for buffer space calculation
        if npc_sequence_overrides and i in npc_sequence_overrides:
            seq_ids = npc_sequence_overrides[i]
            max_seq_vram = 0
            npc = obj._npc
            for seq_id in seq_ids:
                try:
                    v = npc.min_vram_from_sequence(world, seq_id)
                    max_seq_vram = max(max_seq_vram, v)
                except (IndexError, AssertionError):
                    pass
            npc_analysis.max_sequence_vram = max_seq_vram

        npc_analyses.append(npc_analysis)
        i = j

    # --- Step 2: Compute ally buffer size ---
    ally_buffer_size = _calculate_ally_buffer_size(world, room, protagonist)

    # --- Step 3: Assign buffer slots ---
    buffer_assignments, warnings = _assign_buffers_v2(npc_analyses, room_id)

    # --- Step 4: Compute buffer space from sequence overrides ---
    for assignment in buffer_assignments:
        if assignment.buffer_type in (BufferType.FOUR_SPRITES_PER_ROW, BufferType.THREE_SPRITES_PER_ROW):
            assigned_npcs = [n for n in npc_analyses if n.index in assignment.npc_indices]
            if assigned_npcs:
                max_space = max(n.max_sequence_vram for n in assigned_npcs)
                assignment.buffer_space = BufferSpace(min(max_space, 7))

    # --- Step 5: Build result ---
    result = PartitionAnalysis(
        room_id=room_id,
        npcs=npc_analyses,
        ally_buffer_size=ally_buffer_size,
        allow_extra_sprite_buffer=allow_extra_sprite_buffer,
        extra_buffer_size=max_packets,
        buffers=buffer_assignments,
        full_palette=not water,
        warnings=warnings,
    )

    # --- Step 6: Overflow checks ---
    if result.vram_cursor > 32:
        result.warnings.append(
            f"VRAM overflow: cursor={result.vram_cursor} exceeds 32 rows "
            f"(remaining={result.vram_remaining})"
        )
    if result.bitmap_slots_remaining < 0:
        result.warnings.append(
            f"Bitmap slot overflow: {result.bitmap_slots_used} slots used, "
            f"capacity={result.bitmap_slots_capacity} "
            f"(remaining={result.bitmap_slots_remaining})"
        )

    return result


def apply_partition(
    world: GameWorld,
    room_id: int,
    analysis: PartitionAnalysis,
) -> None:
    """Apply a computed partition analysis to a room.

    Sets the room's partition and force_cannot_clone flags on each parent NPC.
    Clones are skipped (they inherit from parent).

    Args:
        world: GameWorld instance.
        room_id: Room index to update.
        analysis: Result from analyze_partition().
    """
    room = world.rooms._rooms[room_id]
    assert room is not None, f"Room {room_id} not found"

    partition = analysis.to_partition()
    partition._full_palette_buffer = analysis.full_palette
    room._partition = partition

    buffered_indices: set[int] = set()
    for assignment in analysis.buffers:
        buffered_indices.update(assignment.npc_indices)

    for npc_analysis in analysis.npcs:
        obj = room.objects[npc_analysis.index]
        if isinstance(obj, Clone):
            continue
        if npc_analysis.force_cannot_clone:
            obj.set_cannot_clone(True)
        elif npc_analysis.index in buffered_indices:
            obj.set_cannot_clone(False)


def filter_fitting_models(
    world: GameWorld,
    room_id: int,
    npc_index: int,
    candidate_models: list,
    *,
    prefer_largest: bool = True,
    **analyze_kwargs,
) -> list[tuple]:
    """Filter and rank NPC models that fit in a room's VRAM budget.

    For each candidate model (a BossNPC subclass with a no-arg constructor and
    a .base attribute returning the NPC definition), temporarily substitutes it
    into the room's NPC slot, runs analyze_partition, and checks vram_remaining >= 0.

    Args:
        world: GameWorld instance.
        room_id: Room to test against.
        npc_index: Object index where the boss NPC sits.
        candidate_models: List of BossNPC subclasses (from prize._npc_models).
            Each must support no-arg construction and have a .base attribute.
        prefer_largest: If True (default), returns sorted largest VRAM first.
            If False, sorted smallest first (for tight rooms).
        **analyze_kwargs: Passed through to analyze_partition (protagonist,
            max_packets, water, npc_sequence_overrides).

    Returns:
        List of (model_class, analysis) tuples for models that fit, sorted by
        VRAM consumption. Empty if nothing fits.
    """
    room = world.rooms._rooms[room_id]
    assert room is not None, f"Room {room_id} not found"
    obj = room.objects[npc_index]
    original_npc = obj._npc

    results = []
    for model_cls in candidate_models:
        model_instance = model_cls()
        obj._npc = model_instance.base
        try:
            analysis = analyze_partition(world, room_id, **analyze_kwargs)
            if analysis.vram_remaining >= 0 and analysis.bitmap_slots_remaining >= 0:
                results.append((model_cls, analysis))
        finally:
            obj._npc = original_npc

    results.sort(key=lambda t: t[1].vram_cursor, reverse=prefer_largest)
    return results


# Bitmap slot cost for the 3 parent slot machine NPCs (all DIR2_SWSE = 1 slot each)
SLOT_MACHINE_BITMAP_COST = 3


def can_room_support_slots(
    world: GameWorld,
    room_id: int,
    **analyze_kwargs,
) -> bool:
    """Check if a room has enough bitmap slots for 5 slot machine NPCs.

    The slot machine adds 3 parent NPCs (FLOWER_NPC_2, STATIC_FROG_COIN_NPC,
    EXPLOSION_NPC) + 2 clones. All are DIR2_SWSE (1 bitmap slot each),
    non-gridplane, cannot_clone=True. Clones share parent VRAM.

    Only the 3 parents consume bitmap slots. Call this BEFORE the slot NPCs
    are placed — it checks whether there's headroom for them.

    Args:
        world: GameWorld instance.
        room_id: Room to test.
        **analyze_kwargs: Passed to analyze_partition (protagonist, max_packets, etc.)

    Returns:
        True if the room can support slot machine NPCs without overflow.
    """
    analysis = analyze_partition(world, room_id, **analyze_kwargs)
    return (
        analysis.bitmap_slots_remaining >= SLOT_MACHINE_BITMAP_COST
        and analysis.vram_remaining >= 0
    )


def analyze_room_partition(
    world: GameWorld,
    room_id: int,
) -> PartitionAnalysis:
    """Analyze a room and compute optimal partition settings.

    This traces each NPC's sprite properties, gridplane format, VramStore type,
    and min_vram requirements to determine the best partition configuration.

    Args:
        world: The GameWorld instance with loaded sprite data.
        room_id: The room index to analyze.

    Returns:
        PartitionAnalysis with optimal settings and diagnostic info.
    """
    from ..types.room import Room

    room = world.rooms._rooms[room_id]
    assert room is not None, f"Room {room_id} not found"

    # Separate regular NPCs from clones.
    # Clones share VRAM with the nearest prior non-clone NPC, so they
    # don't need separate buffer assignments. We count them per parent.
    objects = room.objects
    npc_analyses = []
    i = 0
    while i < len(objects):
        obj = objects[i]
        if isinstance(obj, Clone):
            # Orphan clone (no parent before it) — skip
            i += 1
            continue

        # Count consecutive Clone objects following this NPC
        clone_count = 0
        j = i + 1
        while j < len(objects) and isinstance(objects[j], Clone):
            clone_count += 1
            j += 1

        analysis = _analyze_npc(world, obj, i, clone_count)
        npc_analyses.append(analysis)
        i = j

    # Calculate ally buffer size from room's extra_sprite_actions
    ally_buffer_size = 1  # default minimum
    if isinstance(room, Room) and room.extra_sprite_actions:
        character_model = world.overworld_character.character_model
        if character_model is not None:
            vram_values = []
            for state in DEFAULT_ANIMATION_STATES:
                sprites_dict = character_model.ally._sprites_primary
                if state in sprites_dict:
                    prop_id, offset, is_mold = sprites_dict[state]
                    if is_mold:
                        try:
                            v = character_model._npc.min_vram_from_mold(
                                world, prop_id, offset
                            )
                            vram_values.append(v)
                        except (IndexError, AssertionError):
                            pass
                    else:
                        try:
                            v = character_model._npc.min_vram_from_sequence(
                                world, prop_id, offset
                            )
                            vram_values.append(v)
                        except (IndexError, AssertionError):
                            pass

            for action in room.extra_sprite_actions:
                anim_states = EXTRA_ACTION_TO_ANIMATION_STATE.get(action, [])
                for state in anim_states:
                    sprites_dict = character_model.ally._sprites_primary
                    if state in sprites_dict:
                        prop_id, offset, is_mold = sprites_dict[state]
                        if is_mold:
                            try:
                                v = character_model._npc.min_vram_from_mold(
                                    world, prop_id, offset
                                )
                                vram_values.append(v)
                            except (IndexError, AssertionError):
                                pass
                        else:
                            try:
                                v = character_model._npc.min_vram_from_sequence(
                                    world, prop_id, offset
                                )
                                vram_values.append(v)
                            except (IndexError, AssertionError):
                                pass

            if vram_values:
                ally_buffer_size = min(max(vram_values) + 1, 3)

    # Calculate extra sprite buffer (for chest packet sprites)
    chest_count = sum(1 for n in npc_analyses if n.is_chest)
    allow_extra_sprite_buffer = chest_count > 0
    extra_buffer_size = 0
    if allow_extra_sprite_buffer:
        if room_id in CLOSE_CHEST_ROOMS:
            extra_buffer_size = CLOSE_CHEST_ROOMS[room_id]
        else:
            extra_buffer_size = min(chest_count, 1)

    # Special case: triple empty rooms
    if room_id in TRIPLE_EMPTY_EX1_ROOMS:
        allow_extra_sprite_buffer = True
        extra_buffer_size = 1

    if room_id in TRIPLE_EMPTY_EX0_ROOMS:
        allow_extra_sprite_buffer = False
        extra_buffer_size = 0

    # Determine full palette
    full_palette = True
    if isinstance(room, Room):
        current_partition = room.partition
        if current_partition is not None:
            full_palette = current_partition._full_palette_buffer

    # Assign NPCs to buffers
    buffer_assignments, warnings = _assign_buffers(npc_analyses, room_id)

    # Special case rooms: force triple empty
    if room_id in SPECIAL_CASE_ROOMS:
        has_chest = any(a.buffer_type == BufferType.TREASURE_CHEST for a in buffer_assignments)
        has_coins = any(a.buffer_type == BufferType.COINS for a in buffer_assignments)
        if not has_chest and not has_coins:
            buffer_assignments = [
                BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
                BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
                BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
            ]
            warnings.append("Special case room: forced triple EMPTY_3")

    return PartitionAnalysis(
        room_id=room_id,
        npcs=npc_analyses,
        ally_buffer_size=ally_buffer_size,
        allow_extra_sprite_buffer=allow_extra_sprite_buffer,
        extra_buffer_size=extra_buffer_size,
        buffers=buffer_assignments,
        full_palette=full_palette,
        warnings=warnings,
    )


def apply_partition_analysis(
    world: GameWorld,
    room_id: int,
    analysis: PartitionAnalysis | None = None,
    preserve_ally_buffer: bool = False,
    preserve_extra_sprite_buffer: bool = False,
    preserve_full_palette: bool = False,
) -> PartitionAnalysis:
    """Analyze a room's NPC objects and apply the optimal partition and cannot_clone overrides.

    Computes the partition from scratch (or uses a provided analysis), sets it on the room,
    and sets cannot_clone=True at the room object level for every non-gridplane NPC or NPC
    that needs dedicated VRAM. cannot_clone is set on the room object (not the NPC definition)
    so it acts as an override without affecting other rooms that share the same NPC.

    Args:
        world: The GameWorld instance with loaded sprite data.
        room_id: The room index to analyze and update.
        analysis: Optional pre-computed analysis. If None, calls analyze_room_partition().
        preserve_ally_buffer: If True, keep the room's existing ally_sprite_buffer_size.
        preserve_extra_sprite_buffer: If True, keep the room's existing
            allow_extra_sprite_buffer and extra_sprite_buffer_size.
        preserve_full_palette: If True, keep the room's existing full_palette_buffer.

    Returns:
        The PartitionAnalysis that was applied.
    """
    if analysis is None:
        analysis = analyze_room_partition(world, room_id)

    room = world.rooms._rooms[room_id]
    assert room is not None, f"Room {room_id} not found"

    existing_partition = room.partition

    # Apply the partition
    partition = analysis.to_partition()
    partition._full_palette_buffer = analysis.full_palette

    if existing_partition is not None:
        if preserve_ally_buffer:
            partition.set_ally_sprite_buffer_size(existing_partition.ally_sprite_buffer_size)
        if preserve_extra_sprite_buffer:
            partition.set_allow_extra_sprite_buffer(existing_partition.allow_extra_sprite_buffer)
            partition.set_extra_sprite_buffer_size(existing_partition.extra_sprite_buffer_size)
        if preserve_full_palette:
            partition._full_palette_buffer = existing_partition._full_palette_buffer

    room._partition = partition

    # Determine which NPC indices are assigned to a buffer
    buffered_indices: set[int] = set()
    for assignment in analysis.buffers:
        buffered_indices.update(assignment.npc_indices)

    # Apply cannot_clone overrides at the room object level
    for npc_analysis in analysis.npcs:
        obj = room.objects[npc_analysis.index]
        if isinstance(obj, Clone):
            continue

        if npc_analysis.cannot_clone or npc_analysis.buffer_type == BufferType.EMPTY_3:
            # Non-gridplane or explicitly cannot_clone: needs dedicated VRAM
            obj.set_cannot_clone(True)
        elif npc_analysis.index in buffered_indices:
            # Assigned to a buffer: ensure clone is allowed
            obj.set_cannot_clone(False)

    return analysis