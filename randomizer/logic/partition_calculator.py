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
from ..types.prize import CharacterPrize
from randomizer.logic.progression.prizes import MarioRecruitmentPrize, MallowRecruitmentPrize, GenoRecruitmentPrize, BowserRecruitmentPrize, ToadstoolRecruitmentPrize

import copy
import logging
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
    AREAOBJECT_FROM_NPC_ID as AREA_OBJECTS,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import AreaObject
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import (
    ActionQueueAsync,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import (
    A_IncPaletteRowBy,
)
from randomizer.logic.progression.prizelocations import InnerMinesBossFight
from ..utils.npcs import min_vram_from_sequence_for_sprite
from ..types.prize import BossFightPrize
from ..types.prizelocation import BossFightLocation
from collections import Counter
from ..types.room import Room as ExtRoomForPins
from ..types.room import Room as ExtRoom
from ..data.rooms.npcs import FLOWER_NPC_2, EXPLOSION_NPC
from ..data.rooms.sprite_loader_events import ROOM_SPRITE_LOADER
from ..data.sprites.palette_swap_classes import PURE, SHIFTED
from .palette_rows import rows_remaining
from .renders import (
        _ENDING_CHARACTER_2_NPC_FILLS,
        _ENDING_CHARACTER_3_NPC_FILLS,
        _ENDING_CHARACTER_3_DOLL_FILLS,
        _ENDING_CHARACTER_4_NPC_FILLS,
        _ENDING_CHARACTER_5_NPC_FILLS,
    )
from ..types.room import Room
from ..utils.npcs import (
        PROTAGONIST_BASE_SPRITE_ID,
        PROTAGONIST_SPRITE_RANGE,
        get_protagonist_sprite,
        min_vram_from_sequence_for_sprite,
        min_vram_from_mold_for_sprite,
    )

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld
    from smrpgpatchbuilder.datatypes.levels.classes import BaseRoomObject, NPC, RoomObject
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

    overrides = _get_animation_vram_overrides()

    for override in overrides:
        if override.room_id not in changed_rooms:
            continue

        location = world.locations.get(override.location_class)
        if location is None:
            continue

        assert isinstance(location.prize, BossFightPrize)
        # Prefer the model the placement layer chose for this room; otherwise
        # fall back to a 4096-cap selection that mirrors the legacy behavior.
        npc_model: type | None = None
        if isinstance(location, BossFightLocation):
            npc_model = location.get_chosen_npc_model_for_room(override.room_id)
        if npc_model is None:
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

    changed: set[int] = set([R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE, R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION, R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY, R292_UNMAPPED_HOUSE_ROOM])
    for room_id, vanilla_state in world._vanilla_room_states.items():
        room = world.rooms._rooms[room_id]
        if room is None:
            continue

        # Enumerate current NPC sprites (all objects, Clone is just serialization)
        current_sprites: list[int] = []
        for obj in room.objects:
            current_sprites.append(obj._npc.sprite_id)

        if len(current_sprites) != len(vanilla_state.npcs):
            # NPC count changed (e.g., dummies added) - mark as changed
            changed.add(room_id)
            continue

        for current_sprite_id, vanilla_npc in zip(current_sprites, vanilla_state.npcs):
            if current_sprite_id != vanilla_npc.sprite_id:
                changed.add(room_id)
                break

    return changed


# Rooms that size a declared animation by WHOLE 16x16 tiles instead of by present
# 8x8 subtiles - i.e. min_vram_from_mold_geometry(..., player_sprite=True).
#
# room_id -> the object indices whose dedicated block is sized by whole 16x16 tiles
# instead of present 8x8 subtiles. These are rows of back-to-back cannot_clone
# blocks, where being one unit short corrupts the next NPC instead of landing in
# slack. Subtile packing reads a 5-tile / 13-subtile mold as 0 (13 fits the
# 16-subtile baseline) but the block is 4 tile slots wide, so one tile spills.
# Room 255 = 256 Terrapin/Jagger's dojo_challenge ahead of a zero-slack Belome 3
# Small; room 472 = the three factory_pierce hammer slots, 5 tiles on every model
# that can land there and shipped at 1 in vanilla. Both lists are exactly the
# room's npc_expected_animations keys - neighbours like room 472's Factory Director
# slot are deliberately left on subtile sizing so a shuffled model there is not
# inflated for sequences it never plays.
#
# Both rooms leave buffer A EMPTY, so the cursor may pass its packed $40 base into
# unclaimed VRAM. Do NOT widen this without checking that: whole-tile sizing where
# buffer A is active (rooms 77/78/206/207, chest in A) is the R206 overrun.
WHOLE_TILE_ANIMATION_VRAM_OBJECTS: dict[int, frozenset[int]] = {
    255: frozenset({0, 1, 2, 3, 4}),
    472: frozenset({7, 8, 9}),
}


def _uses_whole_tile_vram(room_id: int, obj_index: int) -> bool:
    """Whether this room object sizes its dedicated block by whole 16x16 tiles."""
    return obj_index in WHOLE_TILE_ANIMATION_VRAM_OBJECTS.get(room_id, frozenset())


def _size_dedicated_min_vram(
    world: GameWorld,
    room_id: int,
    obj_index: int,
    obj: BaseRoomObject,
    sprite_id: int,
    is_gridplane: bool,
) -> None:
    """Raise an NPC's min_vram_size to fit its sprite's largest mold.

    Only meaningful for cannot_clone NPCs: the engine gives them
    4 * (min_vram_size + 1) dedicated tile slots at $C0:8EBC. Undersize it
    and the sprite's tile upload runs past its allocation into the next
    dedicated NPC's slots.

    Gridplane sprites live in a fixed-size block, so min_vram_size stays 0.

    is_gridplane is molds[0].gridplane, so MIXED sprites - gridplane direction
    molds plus tilemap action molds, e.g. 256 Terrapin/Jagger or 764 Poundette -
    would be skipped entirely and keep whatever the NPC record shipped. Lifting
    that early-out globally re-inflates sprite 48 (Croco) in rooms 77/78/206/207
    from the vanilla 0 to 1, which is the R206 chest-buffer overrun, so it is
    lifted only for WHOLE_TILE_ANIMATION_VRAM_OBJECTS.

    Those objects also size by whole 16x16 tiles. Step 5b applies the same rule
    but only to a *placed* shuffled boss/henchman model, never to the room's
    authored occupant - so both paths must honour the mapping or an object with
    shuffling off stays broken.

    Only increases, never decreases - an NPC default may be hand-tuned above
    what the formula computes.
    """
    whole_tile = _uses_whole_tile_vram(room_id, obj_index)
    if is_gridplane and not whole_tile:
        return

    current_min = (
        obj.min_vram_size if obj.min_vram_size is not None else obj._npc.min_vram_size
    )
    sprite = world.get_sprite(sprite_id)
    molds = sprite.animation.properties.molds
    max_vram = current_min
    for seq_idx, seq in enumerate(sprite.animation.properties.sequences):
        for frame in seq.frames:
            if frame.mold_id >= len(molds):
                raise IndexError(
                    f"Room {room_id} NPC {obj_index} (sprite {sprite_id}): "
                    f"sequence {seq_idx} frame references mold_id {frame.mold_id} "
                    f"but sprite only has {len(molds)} molds"
                )
        max_vram = max(
            max_vram,
            min_vram_from_sequence_for_sprite(
                world, sprite_id, seq_idx, player_sprite=whole_tile
            ),
        )

    if max_vram > current_min:
        obj.set_min_vram_size(max_vram)


def _canonical_record(npc: NPC, canonical_sprite_id: int) -> NPC:
    """A copy of npc pointing at canonical_sprite_id.

    Room objects have no usable per-object sprite override -- RegularNPC
    exposes no sprite_id attribute, BaseRoomObject._sprite_id is written by
    set_sprite_id and read by nothing, and both _get_npc_signature and
    _render_npc key on the record. So merging swaps the record instead.

    This MUST copy rather than mutate: NPC records are shared across rooms, and
    mutating one in place corrupts every other room using it. Two objects merged
    onto the same canonical produce records with identical signatures, so
    _get_npc_signature dedups them into a single NPC-table entry and they share
    one clone buffer -- which is the whole point.
    """
    record = copy.copy(npc)
    record.set_sprite_id(canonical_sprite_id)
    return record


# extra_palette_row_count is a 2-bit field, so at most 3 extra CGRAM rows can be
# declared for one palette.
_MAX_PACK_SPAN = 3


_HENCHMAN_MERGE_ROOMS: dict[int, frozenset[int]] | None = None


def _henchman_merge_rooms() -> dict[int, frozenset[int]]:
    """Rooms where two or more henchmen can occupy distinct slots.

    Palette-swap merging is only worth doing where two objects in the same room
    can end up in the same equivalence class, and that is the henchman case: a
    boss whose henchmen are recolours of each other (Culex's crystals,
    Valentina's birds, Johnny's bandanas, Booster's snifits) otherwise burns one
    clone buffer per colour.

    Everything else in the class tables is deliberately out of scope. Item
    sprites fall in the same classes -- a frog coin is a recoloured coin -- but
    merging those can ADD a palette to a room that is already at capacity (Rose
    Way's freestanding items being the known case), which trades a VRAM saving
    for a palette overflow. Non-henchman NPCs also produced the room 197 defect,
    where a HAMMER_PACKET at object 3 took a +2 bump nobody wanted.

    A room with only ONE henchman slot cannot host a collapse, so it is excluded
    too -- that is rooms 17/191/228/230 among others.
    """
    global _HENCHMAN_MERGE_ROOMS
    if _HENCHMAN_MERGE_ROOMS is not None:
        return _HENCHMAN_MERGE_ROOMS

    def subclasses(cls: type) -> list[type]:
        found: list[type] = []
        for sub in cls.__subclasses__():
            found.append(sub)
            found.extend(subclasses(sub))
        return found

    # room id -> object indices that some boss can drop a henchman into
    slots_by_room: dict[int, set[int]] = {}
    for location in subclasses(BossFightLocation):
        # Count SLOT OCCURRENCES, not slots: one BossFightLocationHenchmanNPC can
        # list the same room several times (the ship mooks list room 24 four
        # times), and each occurrence is a separate henchman in that room.
        occurrences: Counter[int] = Counter()
        per_location: dict[int, set[int]] = {}
        for slots in (
            location._character_henchman_slots,
            location._mook_henchman_slots,
        ):
            for slot in slots or []:
                for room_id, npc_id in zip(slot._room_ids, slot._npc_ids):
                    occurrences[int(room_id)] += 1
                    # _npc_ids hold AreaObject values, and AREAOBJECT_FROM_NPC_ID
                    # is NPC_0 == 20, so the object index is the offset from NPC_0.
                    per_location.setdefault(int(room_id), set()).add(
                        int(npc_id) - int(NPC_0)
                    )
        for room_id, indices in per_location.items():
            # A room with only one henchman slot cannot host a collapse.
            if occurrences[room_id] >= 2:
                slots_by_room.setdefault(room_id, set()).update(indices)

    _HENCHMAN_MERGE_ROOMS = {r: frozenset(v) for r, v in slots_by_room.items()}
    return _HENCHMAN_MERGE_ROOMS


def _merge_palette_swaps(world: GameWorld, room_id: int) -> list[tuple[int, int]]:
    """Collapse palette-swap-equivalent sprites in room_id onto one sprite_id.

    A VRAM clone buffer holds exactly one sprite_id and a room has three, so two
    sprites with byte-identical tile data still cost two buffers until they share
    an id.

    Returns [(obj_index, row_bump)] for objects needing A_IncPaletteRowBy queued
    into the room's sprite-loader stub.

    The merge ALWAYS happens (human ruling 2026-07-30). Saving the buffer is the
    point; an NPC rendering in the canonical palette is a cosmetic degradation
    that vanilla itself ships -- rooms 5 and 7 coexist two palette offsets with
    extra_palette_row_count=0. Residency is declared only as far as it fits, and
    never blocks a merge.

    Must run before Step 3 of _recalculate_room_partition, which is where one
    buffer per unique sprite id is decided.
    """
    room = world.rooms._rooms[room_id]
    assert room is not None

    # Opt-in per room. A merged object renders from the CANONICAL sprite's mold
    # set, so a slot that plays an animation the canonical lacks corrupts --
    # room 192's snifits break on mold 6. Only rooms crowded enough to need the
    # freed clone buffer, whose henchmen stay on simple poses, set the flag.
    if not isinstance(room, ExtRoom) or not room.allow_sprite_merging:
        return []

    henchman_indices = _henchman_merge_rooms().get(room_id)
    if not henchman_indices:
        return []

    # Only henchman slots converge. Everything else in the class tables is out of
    # scope: item sprites share classes too (a frog coin is a recoloured coin),
    # but merging one can ADD a palette to a room already at capacity -- Rose
    # Way's freestanding items being the known case -- and non-henchman NPCs
    # produced the room 197 defect, where a HAMMER_PACKET took a +2 nobody wanted.
    candidates = [i for i in henchman_indices if i < len(room.objects)]

    # Tier 1: pure duplicates. No palette work, no stub needed.
    for index in candidates:
        obj = room.objects[index]
        canonical = PURE.get(int(obj._npc.sprite_id))
        if canonical is not None:
            obj._npc = _canonical_record(obj._npc, canonical)

    by_canonical: dict[int, list[tuple[int, int]]] = {}
    for index in candidates:
        entry = SHIFTED.get(int(room.objects[index]._npc.sprite_id))
        if entry is None:
            continue
        canonical, offset = entry
        by_canonical.setdefault(canonical, []).append((index, offset))

    bumps: list[tuple[int, int]] = []
    for canonical, members in by_canonical.items():
        # Every SHIFTED source in the room, plus every object already carrying
        # the canonical sprite, each paired with its OWN intended pack offset.
        # Capture this before any record swapping: once a SHIFTED source's
        # record is swapped to canonical, int(obj._npc.sprite_id) reads as
        # canonical for it too, and it can no longer be told apart from an
        # object that was already canonical to begin with.
        participants: list[tuple[int, int]] = list(members)
        for index in candidates:
            if int(room.objects[index]._npc.sprite_id) == canonical:
                participants.append((index, world.get_sprite(canonical).palette_offset))

        # Nothing to collapse if every participant already holds the same sprite
        # id: they share one clone buffer as they are, so merging frees no VRAM
        # and only makes them depend on a palette-row bump that could fail.
        # Room 154 hit exactly this -- three Snifits (504) merged onto Spookum
        # (282) with no Spookum present, converting three objects that rendered
        # correctly by default into three that rendered canonical blue.
        distinct_sprites = {
            int(room.objects[index]._npc.sprite_id) for index, _ in participants
        }
        if len(distinct_sprites) < 2:
            continue

        # The baseline every merged object renders at is the CANONICAL sprite's
        # own palette_offset, because palette_offset lives on the sprite, not the
        # object -- swapping the record makes an object inherit it. The generator
        # guarantees the canonical holds the class's lowest offset, so every
        # delta below is >= 0 and expressible with A_IncPaletteRowBy.
        canonical_offset = world.get_sprite(canonical).palette_offset

        # Swap records for the SHIFTED sources only -- objects already on the
        # canonical sprite already hold the right record and must not be
        # re-recorded.
        for index, _ in members:
            room.objects[index]._npc = _canonical_record(
                room.objects[index]._npc, canonical
            )

        free = max(0, rows_remaining(world, room))

        # How far past the canonical's row the furthest participant needs to sit.
        # One declaration covers the whole class: the rows are contiguous, so an
        # object needing +1 and one needing +2 share a single 2-row block.
        span = 0
        for _, offset in participants:
            span = max(span, offset - canonical_offset)
        if span <= 0:
            # Everything already renders the canonical's palette; nothing to do.
            continue

        declared = min(span, _MAX_PACK_SPAN, free)
        if declared < span:
            logging.info(
                "room %d: palette %d needs %d extra row(s) but only %d can be "
                "declared (2-bit field caps at %d, %d free) -- objects beyond "
                "that render in the canonical palette instead",
                room_id, world.get_sprite(canonical).palette_id, span, declared,
                _MAX_PACK_SPAN, free,
            )

        # Residency must go on the FIRST object in room order carrying this
        # palette, NOT on the object being recoloured. npc_palette_rows skips
        # later carriers (if palette in rows: continue, palette_rows.py:58) and
        # reads the row count only from the first one, so a declaration on a
        # later object is silently ignored -- the extra row then gets allocated
        # after the intervening palettes instead of adjacent to its own, and the
        # bump lands on whatever NPC sits between. Observed in room 43: NPC 4
        # bumped +1 onto NPC 3's palette while its intended row sat two places
        # further down.
        palette_id = world.get_sprite(canonical).palette_id
        first_carrier = None
        for index, obj in enumerate(room.objects):
            if int(world.get_sprite(int(obj._npc.sprite_id)).palette_id) == palette_id:
                first_carrier = index
                break
        if first_carrier is None:
            continue

        # Source offset is ALWAYS 1, never the delta: it shifts the palette
        # SOURCE pointer, so rows R+1..R+N load palettes base+1..base+N. Writing
        # the delta there lands on base+delta+N-1. Every one of the 821 vanilla
        # NPC records with a row count >= 2 uses source offset 1 (see
        # SHARED_ITEM_BASE in data/rooms/npcs.py, which is 1/2 for an
        # A_IncPaletteRowBy(2)). At delta 1 the two encodings coincide, which is
        # why this only shows up on classes with an offset of 2 or more.
        carrier = room.objects[first_carrier]
        carrier.set_extra_palette_source_offset(1)
        carrier.set_extra_palette_row_count(declared)

        for index, offset in participants:
            delta = offset - canonical_offset
            if 0 < delta <= declared:
                bumps.append((index, delta))

    # Bumps need somewhere to run. Without a stub the sprite_id merge still
    # stands and the VRAM is still saved; only the recolour is lost.
    if room_id not in ROOM_SPRITE_LOADER:
        if bumps:
            logging.info(
                "room %d: no sprite-loader stub, dropping %d palette row bump(s) "
                "-- those objects render in the canonical palette",
                room_id, len(bumps),
            )
        return []

    return bumps


def _emit_palette_bumps(
    world: GameWorld, room_id: int, bumps: list[tuple[int, int]]
) -> int:
    """Queue A_IncPaletteRowBy for each merged object in the room's stub.

    The stub is an empty *_SHUFFLED_NPC_ANIMATION_LOADER already invoked from the
    room's loader as a subroutine.

    Queues are ASYNC. A preloader stub legitimately runs well before the fade and
    before objects are made visible -- room 315 does exactly that and renders
    correctly -- so a Sync queue that completes inline is the wrong shape here.

    NOT fully explained: room 154 reached via script_3809 rendered all three
    merged objects in the canonical palette even though the residency was
    correct (the Snifit palette was resident one row below Spookum, confirmed in
    a debugger) and the bumps were present in stub 790. The same stub reached via
    script_600 was fine. An ordering theory was ruled out by room 315, which has
    the same late-visibility shape and works.
    """
    if not bumps:
        return 0
    event_id = ROOM_SPRITE_LOADER[room_id]
    script = world.get_event_script(event_id)
    for index, delta in bumps:
        script.insert_before_nth_command(
            0,
            ActionQueueAsync(
                target=AREA_OBJECTS[index],
                subscript=[A_IncPaletteRowBy(delta)],
            ),
        )
    return len(bumps)


def _recalculate_room_partition(world: GameWorld, room_id: int) -> None:
    """Recompute buffer layout and cannot_clone for a room after NPC shuffling.

    Looks at the current NPC makeup, determines optimal buffer assignments
    based on sprite frequency, sets cannot_clone accordingly, and preserves
    non-clone-buffer partition settings (ally buffer, extra sprite buffer,
    full palette). Carries over main_buffer_space and index_in_main_buffer
    from the original partition, tracked by NPC slot association.

    Algorithm:
    1. Analyze all NPCs: sprite ID, gridplane format, room-level cannot_clone
    2. Map original buffers to the NPC indices they served
    3. Group sprites by ID and count frequency - counting ONLY NPCs whose
       room-level cannot_clone is None (the auto-decide bucket). NPCs with
       explicit room-level cannot_clone=True/False are excluded so a single
       override-NPC can't disqualify its sprite for other NPCs sharing it.
    4. Assign up to 3 buffer slots (CHEST→0, COINS→2, gridplane by frequency)
    5. Order gridplane buffers to match NPC object order
    6. Set cannot_clone for auto-decide NPCs only: False if their sprite landed
       in a buffer, True otherwise. Room-level overrides are preserved as-is.
    7. Carry over main_buffer_space and index_in_main_buffer from original
       buffers, tracked by NPC slot (not by buffer index or type)
    """
    room = world.rooms._rooms[room_id]
    assert room is not None
    assert room.partition is not None

    # Collapse palette-swap-equivalent sprites before anything counts distinct
    # sprite ids. Step 3 assigns one buffer per unique sprite id, so merging
    # after that point buys nothing.
    _emit_palette_bumps(world, room_id, _merge_palette_swaps(world, room_id))

    existing = room.partition

    # Step 1: Analyze current NPCs
    @dataclass
    class NPCInfo:
        obj_index: int
        sprite_id: int
        is_gridplane: bool
        gridplane_format: int | None  # 0-1 = FOUR, 2-3 = THREE
        is_chest: bool
        is_coin: bool
        force_cannot_clone: bool  # Room-level override - orchestrator must respect
        # Raw room-level cannot_clone value (True/False/None) at recalc-entry.
        # Drives frequency-analysis exclusion (Step 3) and override preservation
        # in Step 7. force_cannot_clone may flip to True later via Step 5b's
        # animation override; original_cannot_clone never changes.
        original_cannot_clone: bool | None

    npc_infos: list[NPCInfo] = []
    for i, obj in enumerate(room.objects):
        sprite_id = obj._npc.sprite_id
        is_gridplane, fmt = _get_npc_gridplane_info(world, sprite_id)
        is_chest = isinstance(obj, ChestNPC) or sprite_id == CHEST_SPRITE_ID
        is_coin = sprite_id in COIN_SPRITE_IDS

        # Room-level cannot_clone=True is a hard structural constraint: the
        # NPC goes in dedicated VRAM regardless of what sprite lands here
        # after shuffling. npc_expected_animations only influences the
        # min_vram_size sizing for that dedicated allocation (handled in
        # step 5b / step 7), not whether the NPC clones.
        force_cc = obj.cannot_clone is True

        npc_infos.append(NPCInfo(
            obj_index=i,
            sprite_id=sprite_id,
            is_gridplane=is_gridplane,
            gridplane_format=fmt,
            is_chest=is_chest,
            is_coin=is_coin,
            force_cannot_clone=force_cc,
            original_cannot_clone=obj.cannot_clone,
        ))

    # Step 3: Determine buffer needs - one buffer per unique sprite ID
    # At runtime, each unique sprite ID gets its own VRAM allocation via
    # the sprite table at $9C4A. Different sprites with the same format
    # do NOT share a buffer - each needs its own slot.
    has_chest = any(n.is_chest for n in npc_infos)
    has_coin = any(n.is_coin for n in npc_infos)

    # Build sprite groups: sprite_id → (buffer_type, npc_count, first_obj_index)
    # Frequency analysis includes NPCs with original_cannot_clone in {None, False};
    # only True is excluded.
    # - None (auto-decide): standard candidate, demand for a buffer slot.
    # - False (explicit opt-in to cloning): the room author has declared this
    #     NPC must ride a clone buffer, so its sprite_id MUST claim a slot -
    #     otherwise step 7 honors the False override and the NPC ends up with
    #     no buffer at all (room 341 GOLD_GOOMBA bug).
    # - True (explicit dedicated VRAM): goes to its own min_vram_size
    #     allocation, doesn't need a clone-buffer slot, and shouldn't disqualify
    #     its sprite for other NPCs that share the sprite_id. (Pre-fix bug: a
    #     force_cannot_clone NPC sharing a sprite with cannot_clone=None NPCs
    #     caused the whole sprite group to be dropped from buffer eligibility,
    #     demoting every NPC sharing that sprite to cannot_clone=True even
    #     though only the override-NPC needed it.)
    sprite_to_type: dict[int, BufferType] = {}  # sprite_id → needed buffer type
    sprite_counts: Counter[int] = Counter()  # auto-decide + explicit-False NPCs counted
    sprite_first_appearance: dict[int, int] = {}  # sprite_id → first obj_index

    for npc_info in npc_infos:
        if npc_info.original_cannot_clone is True:
            continue  # Force-True override owns dedicated VRAM, doesn't claim a slot
        if not npc_info.is_gridplane or npc_info.gridplane_format is None:
            continue
        sprite_id = npc_info.sprite_id
        fmt = npc_info.gridplane_format
        sprite_counts[sprite_id] += 1
        if sprite_id not in sprite_to_type:
            if fmt in (0, 1):
                sprite_to_type[sprite_id] = BufferType.FOUR_SPRITES_PER_ROW
            elif fmt in (2, 3):
                sprite_to_type[sprite_id] = BufferType.THREE_SPRITES_PER_ROW
        if sprite_id not in sprite_first_appearance:
            sprite_first_appearance[sprite_id] = npc_info.obj_index

    for npc in npc_infos:
        if (npc.is_chest or npc.is_coin) and npc.sprite_id in sprite_to_type:
            del sprite_to_type[npc.sprite_id]
            sprite_counts.pop(npc.sprite_id, None)
            sprite_first_appearance.pop(npc.sprite_id, None)

    available_slots = 3
    if has_chest:
        available_slots -= 1
    if has_coin:
        available_slots -= 1

    ranked_sprites = sorted(
        sprite_to_type.keys(),
        key=lambda sid: sprite_counts[sid],
        reverse=True,
    )

    buffered_sprite_ids: set[int] = set()
    selected_buffers: list[tuple[int, BufferType]] = []  # (sprite_id, buffer_type)
    for sprite_id in ranked_sprites:
        if len(selected_buffers) >= available_slots:
            break
        selected_buffers.append((sprite_id, sprite_to_type[sprite_id]))
        buffered_sprite_ids.add(sprite_id)

    # Step 4: Assign buffers, bottom-packing toward slot C
    # Two invariants drive slot assignment:
    #
    #   (A) NPC object order ⇒ slot order.  Within the slots claimed by
    #       gridplane sprites (excluding chest/coin/pin overrides), if NPC_i
    #       appears before NPC_j and both get buffered, NPC_i's slot index
    #       must be <= NPC_j's.
    #
    #   (B) Keep slot 0 EMPTY whenever possible.  An untraced code path in
    #       the engine reads buffer A's format for cannot_clone NPC tile
    #       layout and applies it globally; placing a clone-buffer type
    #       (FOUR_SPR / THREE_SPR) at slot 0 corrupts cannot_clone NPC
    #       renders (see room 110 regression - Boomer peck animation
    #       overwriting the statues - and rooms 205/232 history).
    #
    # Strategy: bottom-pack.  Reserve slot 0 for chests, slot 2 for coins,
    # and pack the remaining gridplane sprites into the bottom-most free
    # slots (high index first), assigning sprites to those slots in NPC
    # object order with ascending slot index.  This guarantees:
    #
    # - 1 sprite, no chest/coin → [EMPTY, EMPTY, sprite]
    # - 2 sprites, no chest/coin → [EMPTY, sprite_first, sprite_second]
    # - chest + 1 sprite → [CHEST, EMPTY, sprite]
    # - chest + coin + 1 sprite → [CHEST, sprite, COIN]
    #
    # Slot 0 stays EMPTY in every layout that doesn't have a chest, which
    # is what the cannot_clone NPC tile-layout path expects.
    selected_buffers.sort(
        key=lambda sb: sprite_first_appearance.get(sb[0], 999),
    )

    new_buffer_types: list[BufferType] = [BufferType.EMPTY_3] * 3

    if has_chest:
        new_buffer_types[0] = BufferType.TREASURE_CHEST
    if has_coin:
        new_buffer_types[2] = BufferType.COINS

    sprite_to_new_buffer: dict[int, int] = {}
    # main_buffer_space overrides produced by vanilla_sprite_buffer_pins
    pinned_slot_bufspace: dict[int, BufferSpace] = {}

    # Step 4a: Apply vanilla_sprite_buffer_pins - if an NPC's current sprite
    # matches its vanilla sprite, force that sprite into the pinned slot
    # before bottom-packing runs.  These overrides are explicit room author
    # choices and take precedence over the bottom-packing default.
    if isinstance(room, ExtRoomForPins) and room.vanilla_sprite_buffer_pins:
        assert world._vanilla_room_states is not None
        vanilla_state_for_pins = world._vanilla_room_states.get(room_id)
        if vanilla_state_for_pins is not None:
            for npc_idx, (slot_idx, bufspace) in room.vanilla_sprite_buffer_pins.items():
                if npc_idx >= len(room.objects) or npc_idx >= len(vanilla_state_for_pins.npcs):
                    continue
                if slot_idx < 0 or slot_idx >= 3:
                    continue
                current_sprite = room.objects[npc_idx]._npc.sprite_id
                vanilla_sprite = vanilla_state_for_pins.npcs[npc_idx].sprite_id
                if current_sprite != vanilla_sprite:
                    continue  # Sprite replaced - pin is ignored
                if current_sprite not in sprite_to_type:
                    continue  # Not a gridplane sprite we can pin
                if new_buffer_types[slot_idx] != BufferType.EMPTY_3:
                    continue  # Slot reserved (chest/coin) or already pinned
                btype = sprite_to_type[current_sprite]
                new_buffer_types[slot_idx] = btype
                sprite_to_new_buffer[current_sprite] = slot_idx
                buffered_sprite_ids.add(current_sprite)
                pinned_slot_bufspace[slot_idx] = bufspace

    # Step 4b: Bottom-pack remaining buffers.
    #
    # free_slots lists unreserved slots ranked bottom-first (slot 2 first).
    # Take the bottom-most N of those free slots for the N unplaced sprites,
    # then sort ascending and zip with sprites in NPC-object-appearance order.
    # Result: earliest NPC's sprite gets the lowest chosen slot index,
    # satisfying invariant (A); slot 0 stays EMPTY unless every higher slot
    # is already reserved.
    unplaced_buffers = [
        (sid, bt) for sid, bt in selected_buffers
        if sid not in sprite_to_new_buffer
    ]

    free_slots = [s for s in (2, 1, 0) if new_buffer_types[s] == BufferType.EMPTY_3]
    n_to_place = min(len(unplaced_buffers), len(free_slots))
    chosen_slots = sorted(free_slots[:n_to_place])

    for (sprite_id, btype), slot in zip(unplaced_buffers[:n_to_place], chosen_slots):
        new_buffer_types[slot] = btype
        sprite_to_new_buffer[sprite_id] = slot

    # Overflow sprites (more distinct gridplane sprites than free slots) get
    # demoted to cannot_clone via step 7's fallback.
    for sprite_id, _ in unplaced_buffers[n_to_place:]:
        buffered_sprite_ids.discard(sprite_id)

    # Step 5: Carry over buffer space and index_in_main_buffer
    # Map vanilla sprites to their original buffer index.  The game engine
    # assigns NPCs to clone buffers by matching sprite ID - the first NPC
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
            # Gridplane buffer - find which sprites are assigned here and
            # carry over buffer space from their VANILLA buffer (if the same
            # sprite was present in vanilla).  For new sprites not in vanilla,
            # use the NPC's min_vram_size as a baseline.
            max_space = 0
            for npc in npc_infos:
                if npc.sprite_id not in buffered_sprite_ids:
                    continue
                if sprite_to_new_buffer.get(npc.sprite_id) != i:
                    continue
                orig_buf_idx = vanilla_sprite_to_buffer.get(npc.sprite_id)
                if orig_buf_idx is not None:
                    # Same sprite in vanilla - carry over its buffer space
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

    # Apply vanilla_sprite_buffer_pins buffer_space overrides (step 4a pins).
    # These take precedence over vanilla-carry-over but lose to step 5b's
    # animation-based sizing if that computes a larger value.
    for slot_idx, pinned_space in pinned_slot_bufspace.items():
        if pinned_space.value > new_buffer_space[slot_idx].value:
            new_buffer_space[slot_idx] = pinned_space

    # Step 5b: Compute animation-based buffer space / min_vram_size
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
    if isinstance(room, ExtRoom) and room.npc_expected_animations:

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
                # Normalize entry shapes:
                #   bare SpriteAnimationState  → treat as ally character animation
                #   ("character", state)       → explicit ally character animation
                #   str                        → boss SpriteAnimationCollection attr
                anim_state: SpriteAnimationState | None = None
                if isinstance(anim_entry, SpriteAnimationState):
                    anim_state = anim_entry
                elif isinstance(anim_entry, tuple) and len(anim_entry) == 2 and anim_entry[0] == "character":
                    anim_state = anim_entry[1]

                if anim_state is not None:
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
                        offset, prop_id, is_mold = sprites_dict[anim_state]
                        try:
                            npc_model = char_prize.character_model
                            if is_mold:
                                vram = npc_model.min_vram_from_mold(world, prop_id, offset)
                            else:
                                vram = npc_model.min_vram_from_sequence(world, prop_id, offset)
                            max_vram_needed = max(max_vram_needed, vram)
                        except (IndexError, AssertionError):
                            pass
                        break
                elif isinstance(anim_entry, str):
                    # Boss / henchman animation attr - search locations for a
                    # placed model whose sprite matches the post-shuffle sprite
                    # in this slot. Both BossNPC and HenchmanNPC subclass
                    # SupplantableNPC, so once we find any model with a matching
                    # sprite_id, the named animation attr resolves uniformly.
                    #
                    # Bosses are recorded by room into _chosen_npc_models_by_room
                    # by the npc_slots placement loop; henchmen are recorded by
                    # (room_id, npc_id) into _chosen_henchman_models_by_room_npc
                    # by the henchman placement loop. We pull both. No room /
                    # NPC class is special-cased here - every location's chosen
                    # models are eligible, and the sprite_id filter below picks
                    # whichever one actually landed in this slot.
                    matched = False
                    for location in world.locations.values():
                        if not isinstance(location, BossFightLocation):
                            continue
                        if not isinstance(location.prize, BossFightPrize):
                            continue
                        candidates: list[type] = list(
                            location.get_all_chosen_npc_models()
                        )
                        candidates.extend(location.get_all_chosen_henchman_models())
                        if not candidates:
                            try:
                                candidates = [
                                    location.prize.get_npc_for_slot(world, 4096)
                                ]
                            except Exception:
                                continue
                        for npc_model in candidates:
                            try:
                                placed = npc_model()
                                if placed.base.sprite_id != sprite_id:
                                    continue
                                if placed.animations is None:
                                    continue
                                animation = getattr(placed.animations, anim_entry, None)
                                if animation is None:
                                    continue
                                seq_id = animation.sequence_id
                                vram = min_vram_from_sequence_for_sprite(
                                    world,
                                    sprite_id,
                                    seq_id,
                                    player_sprite=_uses_whole_tile_vram(room_id, obj_idx),
                                )
                                max_vram_needed = max(max_vram_needed, vram)
                                matched = True
                                break
                            except Exception:
                                continue
                        if matched:
                            break

            if max_vram_needed == 0:
                continue

            # Case 1: Room-level cannot_clone=True - already force_cannot_clone,
            # just ensure min_vram_size is sufficient
            if npc_info and npc_info.force_cannot_clone:
                current_min = obj.min_vram_size if obj.min_vram_size is not None else obj._npc.min_vram_size
                if max_vram_needed > current_min:
                    obj.set_min_vram_size(max_vram_needed)
                continue

            # Case 2: Unique sprite (only 1 NPC with this sprite) - cheaper
            # to use cannot_clone=True + min_vram_size than inflate a buffer
            if sprite_counts.get(sprite_id, 0) <= 1:
                if npc_info and npc_info.sprite_id in buffered_sprite_ids:
                    buffered_sprite_ids.discard(npc_info.sprite_id)
                    buf_idx = sprite_to_new_buffer.pop(npc_info.sprite_id, None)
                    if buf_idx is not None:
                        new_buffer_types[buf_idx] = BufferType.EMPTY_3
                obj.set_cannot_clone(True)
                current_min = obj.min_vram_size if obj.min_vram_size is not None else obj._npc.min_vram_size
                obj.set_min_vram_size(max(max_vram_needed, current_min))
                # Update npc_info so step 7 doesn't override
                if npc_info:
                    npc_info.force_cannot_clone = True
                continue

            # Case 3: Shared sprite (multiple NPCs) - increase buffer space
            if npc_info and npc_info.sprite_id in buffered_sprite_ids:
                buf_idx = sprite_to_new_buffer.get(npc_info.sprite_id)
                if buf_idx is not None:
                    needed_space = BufferSpace(min(max_vram_needed, 7))
                    if needed_space.value > new_buffer_space[buf_idx].value:
                        new_buffer_space[buf_idx] = needed_space
            else:
                # Shared but not in buffer (no slot available) - set min_vram
                obj.set_cannot_clone(True)
                current_min = obj.min_vram_size if obj.min_vram_size is not None else obj._npc.min_vram_size
                obj.set_min_vram_size(max(max_vram_needed, current_min))
                if npc_info:
                    npc_info.force_cannot_clone = True

    # Step 6: Apply buffer changes to the existing partition

    # Rooms whose buffer TYPES must always be preserved from the source partition,
    # regardless of what the orchestrator's analysis would otherwise pick. The
    # orchestrator still updates main_buffer_space, index_in_main_buffer, and
    # per-NPC cannot_clone / min_vram_size, but the buffer-type sequence
    # (THREE_SPRITES_PER_ROW / FOUR_SPRITES_PER_ROW / etc.) stays as authored.
    PRESERVE_BUFFER_TYPES_ROOMS: set[int] = {
        292,  # R292 - split second-half of the R496 ending cutscene; mirrors
              # R496's hand-tuned 3/4/4 layout.
        496,  # R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE - ending cutscene
              # has a hand-tuned 3/4/4 layout that must survive ally_buffer growth.
    }
    if room_id in PRESERVE_BUFFER_TYPES_ROOMS:
        new_buffer_types = [b.buffer_type for b in existing.buffers]

    for i in range(3):
        existing.buffers[i].set_buffer_type(new_buffer_types[i])
        existing.buffers[i].set_main_buffer_space(new_buffer_space[i])
        existing.buffers[i].set_index_in_main_buffer(new_index_in_main[i])

    # Step 7: Set cannot_clone and min_vram_size on all NPCs
    for npc in npc_infos:
        obj = room.objects[npc.obj_index]
        if npc.force_cannot_clone:
            # Room-level override - always dedicated VRAM. Which sprite occupies
            # this slot still varies with boss shuffle, so the allocation must be
            # sized for whatever landed here.
            _size_dedicated_min_vram(
                world, room_id, npc.obj_index, obj, npc.sprite_id, npc.is_gridplane
            )
        elif npc.original_cannot_clone is False:
            # Room author explicitly opted this NPC INTO cloning. Honor it
            # even if the sprite didn't end up in a frequency-selected buffer
            # (responsibility falls on the room author to ensure a buffer
            # exists for the sprite - typically via vanilla_sprite_buffer_pins
            # or by relying on a same-sprite cannot_clone=None NPC alongside).
            pass
        elif npc.is_chest or npc.is_coin:
            obj.set_cannot_clone(False)
        elif npc.sprite_id in buffered_sprite_ids:
            obj.set_cannot_clone(False)
        else:
            obj.set_cannot_clone(True)
            _size_dedicated_min_vram(
                world, room_id, npc.obj_index, obj, npc.sprite_id, npc.is_gridplane
            )

    # Step 8: Log warnings
    if world.settings.debug_mode:
        for npc in npc_infos:
            if npc.force_cannot_clone:
                continue  # Intentionally excluded from buffers


def _get_boss_henchman_rooms(world: GameWorld) -> set[int]:
    """Collect room IDs that have boss, henchman, or statue NPC placements.

    Only these rooms need partition recalculation - other rooms with NPC
    changes (character recruitment, credits, etc.) have stable partitions.
    """

    rooms: set[int] = set()
    for location in world.locations.values():
        if not isinstance(location, BossFightLocation):
            continue
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


def _detect_ending_character_rooms() -> set[int]:
    """Return the set of rooms where ending-cutscene NPC slots get sprite-substituted
    by _apply_ending_character_npc_fills based on which character landed in each
    recruitment slot. The shuffle puts any of {Toadstool, Mallow, Geno, Bowser, Mario}
    minus the protagonist into NPC slots 19-23 of room 496 (and corresponding slots in
    rooms 88, 269, 375, 435, etc.), so the partition for each of these rooms must be
    recalculated post-shuffle to size min_vram_size for whichever sprite actually
    landed there.
    """
    rooms: set[int] = set()
    for fills in (
        _ENDING_CHARACTER_2_NPC_FILLS,
        _ENDING_CHARACTER_3_NPC_FILLS,
        _ENDING_CHARACTER_3_DOLL_FILLS,
        _ENDING_CHARACTER_4_NPC_FILLS,
        _ENDING_CHARACTER_5_NPC_FILLS,
    ):
        for sub in fills:
            rooms.add(sub.room_id)
    return rooms


# Rooms whose partition must NEVER be recalculated. These are the three
# ending-cutscene rooms (88/375/496) where NPC slots, vram sizes, and buffer
# layout are all hand-frozen - the role-swap path keeps each character at
# their permanent NPC slot and only retargets script commands + swaps coords.
# Room 422 (Belome's treasure room) is also locked: empirically, the items
# only render correctly with all three buffers set to EMPTY_3, and the
# partition must stay that way regardless of NPC-shuffle changes.
_NEVER_RECALCULATE_PARTITION_ROOMS: set[int] = {
    R088_SMITHYS_FINAL_FORM_DEFEAT_GENOS_REDEMPTION,
    R292_UNMAPPED_HOUSE_ROOM,
    R375_ENDING_CREDITS_STAR_PIECES_SHOOT_THROUGH_THE_SKY,
    R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
    R496_FACTORY_GROUNDS_FIGHT_WITH_SMITHY_USES_SLEDGE,
}


# Rooms where apply.py swaps an NPC to the alternate-protagonist model
# (ALLY_CLONE_NPC, sprite 31) on non-Mario seeds. The vanilla partition is
# sized for Mario's sprite 0 (gridplane format 1 => FOUR_SPRITES_PER_ROW);
# Mallow and Bowser are format 2/3 and need THREE_SPRITES_PER_ROW, so these
# rooms must go through recalculation. Booster Tower's entrance does the same
# swap but already qualifies as a boss room.
_PROTAGONIST_CLONE_ROOMS: set[int] = {
    R179_SUNKEN_SHIP_POSTKC_AREA_06_MARIO_MIRROR_ROOM,
}


def update_changed_room_partitions(world: GameWorld) -> None:
    """Recalculate partitions for rooms where NPC models changed.

    Recalculates boss/henchman rooms where sprites changed, slot machine rooms,
    ending-cutscene rooms (whose NPC slots get sprite-substituted post-shuffle),
    and protagonist-clone rooms.

    Call order:
    1. Detect changed rooms via snapshot diff
    2. Filter to boss/henchman + slot machine + ending-character + protagonist-clone rooms
    3. Apply animation VRAM overrides (min_vram_size pre-pass)
    4. Recalculate partition for each changed room
    """
    all_changed = _detect_changed_rooms(world)
    boss_rooms = _get_boss_henchman_rooms(world)
    slot_rooms = _detect_slot_machine_rooms(world)
    ending_rooms = _detect_ending_character_rooms()
    changed_rooms = (
        (all_changed & boss_rooms)
        | (all_changed & slot_rooms)
        | (all_changed & ending_rooms)
        | (all_changed & _PROTAGONIST_CLONE_ROOMS)
    )
    changed_rooms -= _NEVER_RECALCULATE_PARTITION_ROOMS

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
    R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM,
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

# The blank sprite. It renders nothing, so it needs neither a clone-buffer slot nor a
# dedicated VRAM allocation - but it IS non-gridplane, and every cannot_clone/buffer
# heuristic reads "non-gridplane" as "needs its own VRAM". The inert placeholders from
# _pre_allocate_dummy_npcs use it in ~95 rooms, so it must be excluded explicitly.
EMPTY_SPRITE_ID = SPR1023_EMPTY


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
    # Raw room-level cannot_clone (True/False/None) before any NPC-level default or
    # heuristic is folded in. cannot_clone above already merges the NPC default, so
    # it cannot distinguish "author explicitly opted into cloning" (False) from
    # "auto-decide" (None). Apply sites need that distinction to honor an explicit
    # False, exactly as _recalculate_room_partition step 7 does.
    original_cannot_clone: bool | None


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

    # Detect by sprite ID, not just class - a RegularNPC with sprite 94
    # still needs TREASURE_CHEST buffer type for VRAM layout purposes.
    is_chest = isinstance(npc_obj, ChestNPC) or sprite_id == CHEST_SPRITE_ID
    is_coin = sprite_id in COIN_SPRITE_IDS

    is_gridplane, gridplane_format = _get_npc_gridplane_info(world, sprite_id)

    # The blank sprite draws nothing: it must claim no buffer slot (EMPTY_3 is excluded
    # from _assign_buffers_v2's four_npcs/three_npcs groups) and take no dedicated VRAM.
    # Checked before the clone_count branch below, which would otherwise hand the
    # placeholder blocks (1 RegularNPC + 4 RegularClones) a FOUR_SPRITES_PER_ROW slot -
    # one of only three - in every slot-eligible room.
    is_empty = sprite_id == EMPTY_SPRITE_ID

    if is_empty:
        buffer_type = BufferType.EMPTY_3
    elif is_chest:
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
    elif clone_count > 0:
        # Shared tilemap (non-gridplane) sprite - multiple NPCs reference
        # one VRAM copy from a clone buffer. Default to FOUR_SPRITES_PER_ROW
        # (the most flexible buffer format for tilemap; engine accepts
        # tilemap data into either FOUR/THREE-per-row buffers, but
        # FOUR-per-row gives more headroom for variable-size molds).
        buffer_type = BufferType.FOUR_SPRITES_PER_ROW
    else:
        buffer_type = BufferType.EMPTY_3

    # NPCs that get dedicated VRAM outside the buffer system:
    # - cannot_clone NPCs (gridplane or not) - the game allocates dedicated VRAM
    # - non-gridplane NPCs that are the SOLE user of their sprite_id -
    #   they can't be referenced from a shared clone-buffer slot, so they
    #   need their own VRAM allocation.
    #
    # Multiple non-gridplane NPCs that share the same sprite_id can ride a
    # single clone-buffer slot (the engine references one VRAM copy from N
    # NPCs, same as gridplane). Forcing those into cannot_clone wastes
    # dedicated slots and corrupts the buffer-allocation calculation.
    # Empirically verified in R232 where ~10 NPCs sharing one tilemap sprite
    # render correctly only when set to cannot_clone=False.
    #
    # The sole-user heuristic only applies to auto-decide NPCs. A room-level
    # cannot_clone=False is the author declaring "this must ride a clone buffer",
    # and must not be silently promoted - mirrors _recalculate_room_partition
    # step 7 (elif original_cannot_clone is False: pass). Without the is None
    # guard, the inert EMPTY placeholders from _pre_allocate_dummy_npcs (sprite
    # 1023: non-gridplane, and solitary wherever no dummy clones trail them) get
    # dedicated VRAM for a sprite that draws nothing.
    force_cannot_clone = (not is_empty) and (
        cannot_clone
        or (
            npc_obj.cannot_clone is None
            and not is_gridplane
            and not is_chest
            and not is_coin
            and clone_count == 0
        )
    )

    return NPCAnalysis(
        index=index,
        sprite_id=sprite_id,
        vram_store=vram_store,
        min_vram=min_vram,
        max_sequence_vram=min_vram,
        cannot_clone=cannot_clone,
        is_chest=is_chest,
        is_coin=is_coin,
        is_gridplane=is_gridplane,
        gridplane_format=gridplane_format,
        buffer_type=buffer_type,
        clone_count=clone_count,
        force_cannot_clone=force_cannot_clone,
        bitmap_slots=VRAM_STORE_BITMAP_SLOTS.get(vram_store, 1),
        original_cannot_clone=npc_obj.cannot_clone,
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
    # for the fill strategy - these NPCs need compatible buffer format
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

    assignments: list[BufferAssignment] = [
        BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
        BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
        BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
    ]

    if chest_npcs:
        assignments[0] = BufferAssignment(
            BufferType.TREASURE_CHEST,
            _calculate_buffer_space(chest_npcs),
            [n.index for n in chest_npcs],
        )

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

    assignments: list[BufferAssignment] = [
        BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
        BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
        BufferAssignment(BufferType.EMPTY_3, BufferSpace.BYTES_0),
    ]

    if chest_npcs:
        assignments[0] = BufferAssignment(
            BufferType.TREASURE_CHEST,
            BufferSpace.BYTES_0,
            [n.index for n in chest_npcs],
        )

    if coin_npcs:
        assignments[2] = BufferAssignment(
            BufferType.COINS,
            BufferSpace.BYTES_0,
            [n.index for n in coin_npcs],
        )

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
            # No empty slot available - force all NPCs in this group to cannot_clone
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

    if protagonist is None:
        return 1

    prizes = _get_protagonist_prizes()
    prize_cls = prizes.get(protagonist.lower())
    if prize_cls is None:
        return 1

    prize = prize_cls()
    ally = prize.ally

    if not isinstance(room, Room) or not room.extra_sprite_actions:
        return 1

    # Use the engine-rendered protagonist sprite, NOT character_model.base.sprite_id.
    # See PROTAGONIST_BASE_SPRITE_ID for the rationale (Mario protagonist = sprite 0,
    # non-Mario = sprite 31 post-remap; character_model.base points at non-protagonist
    # placeholder sprites and is wrong for VRAM partition calculations).
    if ally.index not in PROTAGONIST_BASE_SPRITE_ID:
        return 1
    protagonist_base = PROTAGONIST_BASE_SPRITE_ID[ally.index]

    vram_values: list[int] = []

    def _add_state_vram(state):
        sprites_dict = ally._sprites_primary
        if state not in sprites_dict:
            return
        offset, prop_id, is_mold = sprites_dict[state]
        # Skip offsets outside the protagonist sprite range (those reference
        # unrelated NPC sprites, not protagonist animations).
        if offset >= PROTAGONIST_SPRITE_RANGE:
            return
        # Verify the sprite actually exists at the time of this call. If
        # cosmetics.py hasn't yet written sprites 31-37 with the per-character
        # protagonist data, get_protagonist_sprite returns None / placeholder.
        # Caller should ensure this runs after the remap (see apply.py).
        if get_protagonist_sprite(world, ally.index, offset) is None:
            return
        sid = protagonist_base + offset
        try:
            if is_mold:
                v = min_vram_from_mold_for_sprite(world, sid, prop_id, player_sprite=True)
            else:
                v = min_vram_from_sequence_for_sprite(world, sid, prop_id, player_sprite=True)
            vram_values.append(v)
        except (IndexError, AssertionError):
            pass

    for state in DEFAULT_ANIMATION_STATES:
        _add_state_vram(state)

    for action in room.extra_sprite_actions:
        for state in EXTRA_ACTION_TO_ANIMATION_STATE.get(action, []):
            _add_state_vram(state)

    if not vram_values:
        return 1
    needed = max(vram_values) + 1
    if needed > 3:
        # ally_sprite_buffer_size is a 2-bit partition field (0-3). >3 is not
        # representable. Previous behavior silently capped at 3, masking data
        # bugs. Raise instead so the offending sprite/sequence is identifiable.
        raise ValueError(
            f"_calculate_ally_buffer_size produced needed={needed} (>3). "
            f"vram_values={vram_values}. protagonist={protagonist!r}. "
            f"Either a sprite mold has too many subtiles, or this protagonist "
            f"genuinely cannot fit this room's animation set."
        )
    return needed


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

    Pure computation - no side effects. Deterministic for identical inputs.

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
    are placed - it checks whether there's headroom for them.

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
            # Orphan clone (no parent before it) - skip
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
                    offset, prop_id, is_mold = sprites_dict[state]
                    if is_mold:
                        try:
                            v = npc.min_vram_from_mold(world, prop_id, offset, player_sprite=True)
                            vram_values.append(v)
                        except (IndexError, AssertionError):
                            pass
                    else:
                        try:
                            v = npc.min_vram_from_sequence(world, prop_id, offset, player_sprite=True)
                            vram_values.append(v)
                        except (IndexError, AssertionError):
                            pass

            for action in room.extra_sprite_actions:
                anim_states = EXTRA_ACTION_TO_ANIMATION_STATE.get(action, [])
                for state in anim_states:
                    sprites_dict = ally._sprites_primary
                    if state in sprites_dict:
                        offset, prop_id, is_mold = sprites_dict[state]
                        if is_mold:
                            try:
                                v = npc.min_vram_from_mold(world, prop_id, offset, player_sprite=True)
                                vram_values.append(v)
                            except (IndexError, AssertionError):
                                pass
                        else:
                            try:
                                v = npc.min_vram_from_sequence(world, prop_id, offset, player_sprite=True)
                                vram_values.append(v)
                            except (IndexError, AssertionError):
                                pass

            if vram_values:
                ally_buffer_size = min(max(vram_values) + 1, 3)

    # Preserve extra sprite buffer and full palette from the room's existing
    # partition - other things besides chests (water splash, coins, explosions)
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

    buffered_indices: set[int] = set()
    for assignment in analysis.buffers:
        buffered_indices.update(assignment.npc_indices)

    for npc_analysis in analysis.npcs:
        obj = room.objects[npc_analysis.index]
        if isinstance(obj, Clone):
            continue

        if npc_analysis.original_cannot_clone is False:
            # Room author explicitly opted this NPC INTO cloning. Honor it, same as
            # _recalculate_room_partition step 7. Checked first because an EMPTY
            # placeholder is non-gridplane and therefore always buffer_type EMPTY_3,
            # which would otherwise hand it dedicated VRAM for a sprite that draws
            # nothing.
            pass
        elif npc_analysis.cannot_clone or npc_analysis.buffer_type == BufferType.EMPTY_3:
            # Non-gridplane or explicitly cannot_clone: needs dedicated VRAM
            obj.set_cannot_clone(True)
        elif npc_analysis.index in buffered_indices:
            obj.set_cannot_clone(False)

    return analysis