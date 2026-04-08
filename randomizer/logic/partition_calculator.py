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

        # Enumerate current NPC sprites (all objects, Clone is just serialization)
        current_sprites: list[int] = []
        for obj in room.objects:
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
        sprite_id = obj._npc.sprite_id
        is_gridplane, fmt = _get_npc_gridplane_info(world, sprite_id)
        is_chest = isinstance(obj, ChestNPC) or sprite_id == CHEST_SPRITE_ID
        is_coin = sprite_id in COIN_SPRITE_IDS

        # Room-level cannot_clone=True handling:
        # - If this NPC has npc_expected_animations, the cannot_clone was set
        #   FOR those animations. If the placed sprite doesn't have them,
        #   the reason is gone — let the orchestrator decide.
        # - If no npc_expected_animations, always respect it (other reasons).
        from ..types.room import Room as ExtRoom
        force_cc = False
        if obj.cannot_clone is True:
            if isinstance(room, ExtRoom) and i in room.npc_expected_animations:
                # Check if sprite actually has any of the expected animations
                has_any_animation = False
                for anim_entry in room.npc_expected_animations[i]:
                    if isinstance(anim_entry, tuple) and len(anim_entry) == 2 and anim_entry[0] == "character":
                        # Character animation — check if any CharacterPrize has this sprite + state
                        from ..types.prize import CharacterPrize
                        anim_state = anim_entry[1]
                        for location in world.locations.values():
                            if not hasattr(location, 'prize') or not isinstance(location.prize, CharacterPrize):
                                continue
                            if location.prize.character_model.base.sprite_id != sprite_id:
                                continue
                            ally = location.prize.ally
                            sprites_dict = ally._sprites_primary if ally.index == 0 else ally._sprites_secondary
                            if anim_state in sprites_dict:
                                has_any_animation = True
                                break
                    elif isinstance(anim_entry, str):
                        # Boss animation attr
                        for location in world.locations.values():
                            from ..types.prize import BossFightPrize
                            if not hasattr(location, 'prize') or not isinstance(location.prize, BossFightPrize):
                                continue
                            try:
                                npc_model = location.prize.get_npc_for_slot(world, 4096)
                                boss = npc_model()
                                if boss.base.sprite_id != sprite_id:
                                    continue
                                if boss.animations and getattr(boss.animations, anim_entry, None) is not None:
                                    has_any_animation = True
                                    break
                            except Exception:
                                continue
                    if has_any_animation:
                        break
                force_cc = has_any_animation
            else:
                # No expected_animations declared — always respect cannot_clone=True
                force_cc = True

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
    # Step 3: Determine buffer needs — one buffer per unique sprite ID
    # =========================================================================
    # At runtime, each unique sprite ID gets its own VRAM allocation via
    # the sprite table at $9C4A. Different sprites with the same format
    # do NOT share a buffer — each needs its own slot.
    has_chest = any(n.is_chest for n in npc_infos)
    has_coin = any(n.is_coin for n in npc_infos)

    # Build sprite groups: sprite_id → (buffer_type, npc_count, first_obj_index)
    # Count ALL objects (including clones) per sprite for frequency ranking,
    # since clones with the same sprite ID share VRAM and benefit from buffers.
    from collections import Counter
    sprite_to_type: dict[int, BufferType] = {}  # sprite_id → needed buffer type
    sprite_counts: Counter[int] = Counter()  # includes clones for ranking
    sprite_first_appearance: dict[int, int] = {}  # sprite_id → first obj_index

    # Count ALL objects (including clones) and register their sprite types.
    # Clones can have different sprites than their parent after shuffling,
    # and still need buffer consideration.
    for i, obj in enumerate(room.objects):
        sprite_id = obj._npc.sprite_id
        is_gp, fmt = _get_npc_gridplane_info(world, sprite_id)
        if not is_gp or fmt is None:
            continue
        sprite_counts[sprite_id] += 1
        if sprite_id not in sprite_to_type:
            if fmt in (0, 1):
                sprite_to_type[sprite_id] = BufferType.FOUR_SPRITES_PER_ROW
            elif fmt in (2, 3):
                sprite_to_type[sprite_id] = BufferType.THREE_SPRITES_PER_ROW
        if sprite_id not in sprite_first_appearance:
            sprite_first_appearance[sprite_id] = i

    # Remove sprites whose parent NPC has force_cannot_clone
    for npc in npc_infos:
        if npc.force_cannot_clone and npc.sprite_id in sprite_to_type:
            del sprite_to_type[npc.sprite_id]
            sprite_counts.pop(npc.sprite_id, None)
            sprite_first_appearance.pop(npc.sprite_id, None)

    # Also remove chest/coin sprites from gridplane consideration
    for npc in npc_infos:
        if (npc.is_chest or npc.is_coin) and npc.sprite_id in sprite_to_type:
            del sprite_to_type[npc.sprite_id]
            sprite_counts.pop(npc.sprite_id, None)
            sprite_first_appearance.pop(npc.sprite_id, None)

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
    # Step 5: Carry over buffer space and index_in_main_buffer
    # =========================================================================
    # Map vanilla sprites to their original buffer index.  The game engine
    # assigns NPCs to clone buffers by matching sprite ID — the first NPC
    # with a new sprite claims the next available buffer of the right type.
    # We replicate that walk to build vanilla_sprite_to_buffer.
    assert world._vanilla_room_states is not None
    vanilla_state = world._vanilla_room_states.get(room_id)

    vanilla_sprite_to_buffer: dict[int, int] = {}  # vanilla sprite_id → buffer index
    if vanilla_state is not None:
        # Available buffer indices per type (consumed as sprites claim them)
        avail_by_type: dict[BufferType, list[int]] = {}
        for buf_i, buf in enumerate(existing.buffers):
            bt = buf.buffer_type
            if bt not in avail_by_type:
                avail_by_type[bt] = []
            avail_by_type[bt].append(buf_i)

        for vnpc in vanilla_state.npcs:
            if vnpc.sprite_id in vanilla_sprite_to_buffer:
                continue  # Already assigned (shares buffer with earlier NPC)
            if vnpc.is_gridplane and vnpc.gridplane_format is not None:
                if vnpc.gridplane_format in (0, 1):
                    needed = BufferType.FOUR_SPRITES_PER_ROW
                else:
                    needed = BufferType.THREE_SPRITES_PER_ROW
                indices = avail_by_type.get(needed, [])
                if indices:
                    vanilla_sprite_to_buffer[vnpc.sprite_id] = indices.pop(0)

    new_buffer_space: list[BufferSpace] = [BufferSpace.BYTES_0] * 3
    new_index_in_main: list[bool] = [True] * 3  # Default is True

    for i, btype in enumerate(new_buffer_types):
        if btype in (BufferType.TREASURE_CHEST, BufferType.COINS, BufferType.EMPTY_3):
            # For chest/coin/empty, carry over from original matching buffer
            for orig_buf in existing.buffers:
                if orig_buf.buffer_type == btype:
                    new_buffer_space[i] = orig_buf.main_buffer_space
                    new_index_in_main[i] = orig_buf.index_in_main_buffer
                    break
        else:
            # Gridplane buffer — find which sprites are assigned here and
            # carry over buffer space from their VANILLA buffer (if the same
            # sprite was present in vanilla).  For new sprites not in vanilla,
            # use the NPC's min_vram_size as a baseline.
            max_space = 0
            for npc in npc_infos:
                if npc.sprite_id not in buffered_sprite_ids:
                    continue
                if sprite_to_new_buffer.get(npc.sprite_id) != i:
                    continue
                # Check if this sprite was in a vanilla buffer
                orig_buf_idx = vanilla_sprite_to_buffer.get(npc.sprite_id)
                if orig_buf_idx is not None:
                    # Same sprite in vanilla — carry over its buffer space
                    orig_space = existing.buffers[orig_buf_idx].main_buffer_space.value
                    if orig_space > max_space:
                        max_space = orig_space
                # New sprites default to BYTES_0; animation overrides
                # in Step 5b will increase if needed.
            new_buffer_space[i] = BufferSpace(min(max_space, 7))
            # Carry over index_in_main_buffer from original buffer of same type
            for orig_buf in existing.buffers:
                if orig_buf.buffer_type == btype:
                    new_index_in_main[i] = orig_buf.index_in_main_buffer
                    break

    # =========================================================================
    # Step 5b: Compute animation-based buffer space / min_vram_size
    # =========================================================================
    # If the room declares expected_animations for any NPC slot, look up
    # the current sprite's animation sequences and compute needed VRAM.
    #
    # Hierarchy:
    # 1. Room-level cannot_clone=True → already respected (force_cannot_clone),
    #    just set min_vram_size for the animation
    # 2. Unique sprite (count=1) with extra animations → set cannot_clone=True
    #    + min_vram_size (cheaper than inflating a whole buffer)
    # 3. Shared sprite (count>1) with extra animations → keep in buffer,
    #    increase main_buffer_space (more efficient than N dedicated allocations)
    from ..types.room import Room as ExtRoom
    if isinstance(room, ExtRoom) and room.npc_expected_animations:
        from ..utils.npcs import min_vram_from_sequence_for_sprite

        for obj_idx, anim_attrs in room.npc_expected_animations.items():
            obj = room.objects[obj_idx]
            sprite_id = obj._npc.sprite_id
            npc_info = next((n for n in npc_infos if n.obj_index == obj_idx), None)

            # Compute max VRAM needed across all expected animations.
            # Two types of entries:
            #   str → boss animation attr (e.g., "bandits_way_distracted")
            #   ("character", SpriteAnimationState) → character animation state
            max_vram_needed = 0
            for anim_entry in anim_attrs:
                if isinstance(anim_entry, tuple) and len(anim_entry) == 2 and anim_entry[0] == "character":
                    # Character animation — look up via CharacterPrize ally sprites
                    from ..types.prize import CharacterPrize
                    anim_state = anim_entry[1]
                    for location in world.locations.values():
                        if not hasattr(location, 'prize') or not isinstance(location.prize, CharacterPrize):
                            continue
                        char_prize = location.prize
                        if char_prize.character_model.base.sprite_id != sprite_id:
                            continue
                        # Use _sprites_secondary for recruited NPCs (they're not the protagonist)
                        # Use _sprites_primary if the character is Mario (ally index 0)
                        if char_prize.ally.index == 0:
                            sprites_dict = char_prize.ally._sprites_primary
                        else:
                            sprites_dict = char_prize.ally._sprites_secondary
                        if anim_state not in sprites_dict:
                            continue
                        prop_id, offset, is_mold = sprites_dict[anim_state]
                        try:
                            npc_model = char_prize.character_model
                            if is_mold:
                                vram = npc_model._npc.min_vram_from_mold(world, prop_id, offset)
                            else:
                                vram = npc_model._npc.min_vram_from_sequence(world, prop_id, offset)
                            max_vram_needed = max(max_vram_needed, vram)
                        except (IndexError, AssertionError):
                            pass
                        break
                elif isinstance(anim_entry, str):
                    # Boss animation attr — search locations for matching sprite
                    for location in world.locations.values():
                        from ..types.prize import BossFightPrize
                        if not hasattr(location, 'prize') or not isinstance(location.prize, BossFightPrize):
                            continue
                        try:
                            npc_model = location.prize.get_npc_for_slot(world, 4096)
                            boss = npc_model()
                            if boss.base.sprite_id != sprite_id:
                                continue
                            if boss.animations is None:
                                continue
                            animation = getattr(boss.animations, anim_entry, None)
                            if animation is None:
                                continue
                            seq_id = animation.sequence_id
                            vram = min_vram_from_sequence_for_sprite(world, sprite_id, seq_id)
                            max_vram_needed = max(max_vram_needed, vram)
                            break
                        except Exception:
                            continue

            if max_vram_needed == 0:
                continue

            # Case 1: Room-level cannot_clone=True — already force_cannot_clone,
            # just ensure min_vram_size is sufficient
            if npc_info and npc_info.force_cannot_clone:
                current_min = obj.min_vram_size if obj.min_vram_size is not None else obj._npc.min_vram_size
                if max_vram_needed > current_min:
                    obj.set_min_vram_size(max_vram_needed)
                continue

            # Case 2: Unique sprite (only 1 NPC with this sprite) — cheaper
            # to use cannot_clone=True + min_vram_size than inflate a buffer
            if sprite_counts.get(sprite_id, 0) <= 1:
                # Pull from buffer if it was assigned one
                if npc_info and npc_info.sprite_id in buffered_sprite_ids:
                    buffered_sprite_ids.discard(npc_info.sprite_id)
                    buf_idx = sprite_to_new_buffer.pop(npc_info.sprite_id, None)
                    if buf_idx is not None:
                        new_buffer_types[buf_idx] = BufferType.EMPTY_3
                obj.set_cannot_clone(True)
                obj.set_min_vram_size(max_vram_needed)
                # Update npc_info so step 7 doesn't override
                if npc_info:
                    npc_info.force_cannot_clone = True
                continue

            # Case 3: Shared sprite (multiple NPCs) — increase buffer space
            if npc_info and npc_info.sprite_id in buffered_sprite_ids:
                buf_idx = sprite_to_new_buffer.get(npc_info.sprite_id)
                if buf_idx is not None:
                    needed_space = BufferSpace(min(max_vram_needed, 7))
                    if needed_space.value > new_buffer_space[buf_idx].value:
                        new_buffer_space[buf_idx] = needed_space
            else:
                # Shared but not in buffer (no slot available) — set min_vram
                obj.set_cannot_clone(True)
                obj.set_min_vram_size(max_vram_needed)
                if npc_info:
                    npc_info.force_cannot_clone = True

    # =========================================================================
    # Step 6: Apply buffer changes to the existing partition
    # =========================================================================
    if world.settings.debug_mode and room_id == 254:
        print(f"[PARTITION DBG] Room 254:")
        for i, obj in enumerate(room.objects):
            npc_info = next((n for n in npc_infos if n.obj_index == i), None)
            fc = npc_info.force_cannot_clone if npc_info else "?"
            gp = npc_info.is_gridplane if npc_info else "?"
            fmt = npc_info.gridplane_format if npc_info else "?"
            buffered = npc_info.sprite_id in buffered_sprite_ids if npc_info else "?"
            print(f"  obj[{i}]: sprite={obj._npc.sprite_id} force_cc={fc} gridplane={gp} fmt={fmt} buffered={buffered}")
        print(f"  buffers: {[(bt.name, bs.name) for bt, bs in zip(new_buffer_types, new_buffer_space)]}")
        print(f"  buffered_sprite_ids: {buffered_sprite_ids}")
        print(f"  sprite_to_new_buffer: {sprite_to_new_buffer}")

    for i in range(3):
        existing.buffers[i].set_buffer_type(new_buffer_types[i])
        existing.buffers[i].set_main_buffer_space(new_buffer_space[i])
        existing.buffers[i].set_index_in_main_buffer(new_index_in_main[i])

    # =========================================================================
    # Step 7: Set cannot_clone and min_vram_size on all NPCs
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
            # Non-gridplane cannot_clone NPCs need min_vram_size set based on
            # their sprite's largest mold. Without this, the game allocates 0
            # extra VRAM rows and they overwrite other sprites.
            # NOTE: Only increase min_vram, never decrease — the NPC default
            # may be hand-tuned to a value higher than what the formula computes
            # (the formula's baseline assumption can underestimate).
            if not npc.is_gridplane:
                from ..utils.npcs import min_vram_from_sequence_for_sprite
                current_min = obj.min_vram_size if obj.min_vram_size is not None else obj._npc.min_vram_size
                max_vram = current_min
                sprite = world.get_sprite(npc.sprite_id)
                for seq_idx in range(len(sprite.animation.properties.sequences)):
                    seq = sprite.animation.properties.sequences[seq_idx]
                    for frame in seq.frames:
                        if frame.mold_id >= len(sprite.animation.properties.molds):
                            raise IndexError(
                                f"Room {room_id} NPC {npc.obj_index} (sprite {npc.sprite_id}): "
                                f"sequence {seq_idx} frame references mold_id {frame.mold_id} "
                                f"but sprite only has {len(sprite.animation.properties.molds)} molds"
                            )
                    vram = min_vram_from_sequence_for_sprite(world, npc.sprite_id, seq_idx)
                    if vram > max_vram:
                        max_vram = vram
                if max_vram > current_min:
                    obj.set_min_vram_size(max_vram)

    # =========================================================================
    # Step 8: Log warnings
    # =========================================================================
    # Check for sprites that needed a buffer but didn't get one
    if world.settings.debug_mode:
        for npc in npc_infos:
            if npc.force_cannot_clone:
                continue  # Intentionally excluded from buffers
            if npc.is_gridplane and npc.sprite_id not in buffered_sprite_ids and not npc.is_chest and not npc.is_coin:
                print(
                    f"[PARTITION WARN] Room {room_id}: NPC {npc.obj_index} "
                    f"(sprite {npc.sprite_id}, format {npc.gridplane_format}) "
                    f"has no matching buffer, set to cannot_clone=True"
                )


def _get_boss_henchman_rooms(world: GameWorld) -> set[int]:
    """Collect room IDs that have boss, henchman, or statue NPC placements.

    Only these rooms need partition recalculation — other rooms with NPC
    changes (character recruitment, credits, etc.) have stable partitions.
    """
    from ..types.prizelocation import BossFightLocation

    rooms: set[int] = set()
    for location in world.locations.values():
        if not isinstance(location, BossFightLocation):
            continue
        # Collect rooms from all NPC slot types
        for slot_attr in ('_npc_slots', '_character_henchman_slots', '_mook_henchman_slots', '_tiny_henchman_slots', '_statue_slots'):
            slots = getattr(location, slot_attr, None)
            if slots is None:
                continue
            for slot in slots:
                if hasattr(slot, 'room_ids'):
                    for r in slot.room_ids:
                        rooms.add(r)
                elif hasattr(slot, 'room_id'):
                    rooms.add(slot.room_id)
    return rooms


def _detect_slot_machine_rooms(world: GameWorld) -> set[int]:
    """Return room IDs where a SlotsPrize was placed.

    SlotsPrize replaces 5 dummy EMPTY_NPCs with actual slot machine sprites
    (flower, frog coin, explosion). These rooms need partition recalculation
    even though they aren't boss/henchman rooms.
    """
    from ..data.rooms.npcs import FLOWER_NPC_2, EXPLOSION_NPC
    slot_sprite_ids = {FLOWER_NPC_2.sprite_id, EXPLOSION_NPC.sprite_id}

    rooms: set[int] = set()
    for room_id in world._vanilla_room_states:
        room = world.rooms._rooms[room_id]
        if room is None:
            continue
        for obj in room.objects:
            if isinstance(obj, Clone):
                continue
            if obj._npc.sprite_id in slot_sprite_ids:
                rooms.add(room_id)
                break

    return rooms


def update_changed_room_partitions(world: GameWorld) -> None:
    """Recalculate partitions for rooms where NPC models changed.

    Recalculates boss/henchman rooms where sprites changed, plus any room
    that received slot machine NPCs (SlotsPrize).

    Call order:
    1. Detect changed rooms via snapshot diff
    2. Filter to boss/henchman rooms + slot machine rooms
    3. Apply animation VRAM overrides (min_vram_size pre-pass)
    4. Recalculate partition for each changed room
    """
    all_changed = _detect_changed_rooms(world)
    boss_rooms = _get_boss_henchman_rooms(world)
    slot_rooms = _detect_slot_machine_rooms(world)
    changed_rooms = (all_changed & boss_rooms) | (all_changed & slot_rooms)

    if world.settings.debug_mode:
        print(f"[PARTITION] all_changed={len(all_changed)} boss_rooms={len(boss_rooms)} "
              f"slot_rooms={len(slot_rooms)} recalculating={len(changed_rooms)}")
        if changed_rooms:
            print(f"[PARTITION] rooms: {sorted(changed_rooms)}")

    # Pre-pass: animation VRAM overrides
    _apply_animation_vram_overrides(world, changed_rooms)

    # Main pass: recalculate partition for each changed room
    for room_id in changed_rooms:
        _recalculate_room_partition(world, room_id)


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
        """Extra sprite bitmap slots consumed by dynamic (non-clone-buffer) NPCs.

        Only force_cannot_clone NPCs allocate from the extra sprite bitmap at
        $01B2.  Gridplane NPCs in clone buffers, chest NPCs, and coin NPCs use
        the buffer system and never touch the bitmap.
        """
        return sum(npc.bitmap_slots for npc in self.npcs if npc.force_cannot_clone)

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

    prize = prize_cls()
    npc = prize.character_model
    ally = prize.ally

    if not isinstance(room, Room) or not room.extra_sprite_actions:
        return 1

    vram_values: list[int] = []

    # Check default animation states
    for state in DEFAULT_ANIMATION_STATES:
        sprites_dict = ally._sprites_primary
        if state in sprites_dict:
            prop_id, offset, is_mold = sprites_dict[state]
            if is_mold:
                try:
                    v = npc.min_vram_from_mold(world, prop_id, offset)
                    vram_values.append(v)
                except (IndexError, AssertionError):
                    pass
            else:
                try:
                    v = npc.min_vram_from_sequence(world, prop_id, offset)
                    vram_values.append(v)
                except (IndexError, AssertionError):
                    pass

    # Check room's extra_sprite_actions
    for action in room.extra_sprite_actions:
        anim_states = EXTRA_ACTION_TO_ANIMATION_STATE.get(action, [])
        for state in anim_states:
            sprites_dict = ally._sprites_primary
            if state in sprites_dict:
                prop_id, offset, is_mold = sprites_dict[state]
                if is_mold:
                    try:
                        v = npc.min_vram_from_mold(world, prop_id, offset)
                        vram_values.append(v)
                    except (IndexError, AssertionError):
                        pass
                else:
                    try:
                        v = npc.min_vram_from_sequence(world, prop_id, offset)
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
        overworld_prize = world.overworld_character
        npc = overworld_prize.character_model
        ally = overworld_prize.ally
        if npc is not None:
            vram_values = []
            for state in DEFAULT_ANIMATION_STATES:
                sprites_dict = ally._sprites_primary
                if state in sprites_dict:
                    prop_id, offset, is_mold = sprites_dict[state]
                    if is_mold:
                        try:
                            v = npc.min_vram_from_mold(world, prop_id, offset)
                            vram_values.append(v)
                        except (IndexError, AssertionError):
                            pass
                    else:
                        try:
                            v = npc.min_vram_from_sequence(world, prop_id, offset)
                            vram_values.append(v)
                        except (IndexError, AssertionError):
                            pass

            for action in room.extra_sprite_actions:
                anim_states = EXTRA_ACTION_TO_ANIMATION_STATE.get(action, [])
                for state in anim_states:
                    sprites_dict = ally._sprites_primary
                    if state in sprites_dict:
                        prop_id, offset, is_mold = sprites_dict[state]
                        if is_mold:
                            try:
                                v = npc.min_vram_from_mold(world, prop_id, offset)
                                vram_values.append(v)
                            except (IndexError, AssertionError):
                                pass
                        else:
                            try:
                                v = npc.min_vram_from_sequence(world, prop_id, offset)
                                vram_values.append(v)
                            except (IndexError, AssertionError):
                                pass

            if vram_values:
                ally_buffer_size = min(max(vram_values) + 1, 3)

    # Preserve extra sprite buffer and full palette from the room's existing
    # partition — other things besides chests (water splash, coins, explosions)
    # can use packets, so don't override the room definition.
    allow_extra_sprite_buffer = False
    extra_buffer_size = 0
    full_palette = True
    if isinstance(room, Room) and room.partition is not None:
        current_partition = room.partition
        allow_extra_sprite_buffer = current_partition.allow_extra_sprite_buffer
        extra_buffer_size = current_partition.extra_sprite_buffer_size
        full_palette = current_partition._full_palette_buffer

    # Special case: triple empty rooms
    if room_id in TRIPLE_EMPTY_EX1_ROOMS:
        allow_extra_sprite_buffer = True
        extra_buffer_size = 1

    if room_id in TRIPLE_EMPTY_EX0_ROOMS:
        allow_extra_sprite_buffer = False
        extra_buffer_size = 0

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