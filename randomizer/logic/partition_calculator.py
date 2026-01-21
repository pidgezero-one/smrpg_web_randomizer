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

import copy
from math import ceil
from typing import TYPE_CHECKING, Any
from ..data.variables.sprite_names import *
from ..data.variables.room_names import *

from smrpgpatchbuilder.datatypes.levels.classes import (
    Buffer,
    BufferSpace,
    BufferType,
    Partition,
    RegularNPC,
    ChestNPC,
    BattlePackClone,
    RegularClone,
    ChestClone,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import (
    A_SetSpriteSequence as SetSpriteSequence,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.types.classes import (
    ActionSubcriptCommandPrototype,
)
from ..types.room import ExtraSpriteActions, Room
from ..types.ally import SpriteAnimationState, Ally
from ..types.prize import FrogCoinPrize
from ..types.prizelocation import TreasureChestLocation

if TYPE_CHECKING:
    from ..types.gameworld import GameWorld
    from smrpgpatchbuilder.datatypes.levels.classes import RoomObject, Clone
    from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite


# =============================================================================
# Mapping from ExtraSpriteActions to SpriteAnimationState
# Used to determine which ally animation states are needed for each room action
# =============================================================================

EXTRA_ACTION_TO_ANIMATION_STATE: dict[
    ExtraSpriteActions, list[SpriteAnimationState]
] = {
    # Direct matches
    ExtraSpriteActions.DEFEND: [SpriteAnimationState.DEFEND],
    ExtraSpriteActions.SALUTE: [SpriteAnimationState.SALUTE],
    ExtraSpriteActions.CHALLENGE: [SpriteAnimationState.CHALLENGE],
    ExtraSpriteActions.SLEEP: [SpriteAnimationState.SLEEPING],
    # Surprise/shock animations
    ExtraSpriteActions.SURPRISE_FRAME: [
        SpriteAnimationState.SHOCKED_LOOP,
        SpriteAnimationState.SHOCKED_SHADOW,
    ],
    ExtraSpriteActions.SURPRISE_FRAME_BACK: [
        SpriteAnimationState.SHOCKED_LOOP_BACKWARDS,
        SpriteAnimationState.SHOCKED_SHADOW_BACKWARDS,
        SpriteAnimationState.SHOCKED_BACKWARDS_SEQUENCE,
    ],
    # Standing/leaning animations
    ExtraSpriteActions.STANDING_SLEEP: [SpriteAnimationState.SLEEPING],
    ExtraSpriteActions.LEAN_BACK: [SpriteAnimationState.LOOKING_DOWN],
    ExtraSpriteActions.LEAN_BACK_2: [SpriteAnimationState.LOOKING_DOWN_AWAY],
    ExtraSpriteActions.LEAN_FORWARD: [SpriteAnimationState.LOOKING_DOWN_STATIC],
    # Displeased animations
    ExtraSpriteActions.DISPLEASED_FRONT: [SpriteAnimationState.DISPLEASED],
    ExtraSpriteActions.DISPLEASED_BACK: [SpriteAnimationState.DISPLEASED],
    # Praise/joy animations
    ExtraSpriteActions.PRAISE_FRONT: [
        SpriteAnimationState.JOY,
        SpriteAnimationState.JOY_JUMP,
    ],
    ExtraSpriteActions.PRAISE_BACK: [SpriteAnimationState.JOY_BEHIND],
    # Tumble/hurt animations
    ExtraSpriteActions.TUMBLE_FRONT: [
        SpriteAnimationState.FLOORED,
        SpriteAnimationState.HURT,
    ],
    ExtraSpriteActions.TUMBLE_BACK: [
        SpriteAnimationState.FLOORED,
        SpriteAnimationState.HURT,
    ],
    ExtraSpriteActions.RECOIL: [SpriteAnimationState.HURT],
    ExtraSpriteActions.FLOP: [SpriteAnimationState.FLOORED],
    ExtraSpriteActions.DIZZY: [SpriteAnimationState.SHAKING_HEAD],
    ExtraSpriteActions.WOBBLE: [SpriteAnimationState.SHAKING_HEAD],
    # Looking animations
    ExtraSpriteActions.LOOK_AT_DOLL: [
        SpriteAnimationState.LOOK_TO_SIDE,
        SpriteAnimationState.LOOK_TO_DOWN,
    ],
    ExtraSpriteActions.EXOR: [SpriteAnimationState.LOOK_WAY_UP],
    # Challenge variants
    ExtraSpriteActions.CHALLENGE_NIMBUS: [SpriteAnimationState.CHALLENGE],
    # Special animations - map to base states as fallback
    ExtraSpriteActions.SWIM: [SpriteAnimationState.SOUTH],
    ExtraSpriteActions.WHIRL: [SpriteAnimationState.SOUTH],
    ExtraSpriteActions.DOWN_PIPE: [SpriteAnimationState.SOUTH],
    ExtraSpriteActions.CROUCH: [SpriteAnimationState.LOOKING_DOWN_STATIC],
    ExtraSpriteActions.YOSHI: [SpriteAnimationState.SOUTH],
    ExtraSpriteActions.CLIMB: [SpriteAnimationState.FACE_NORTH],
    ExtraSpriteActions.CLIMB_FRAME: [SpriteAnimationState.FACE_NORTH],
    ExtraSpriteActions.BLACKJACK: [SpriteAnimationState.SOUTH],
    ExtraSpriteActions.HOLD_STAR: [SpriteAnimationState.VICTORY_POSE],
    ExtraSpriteActions.MUTE: [SpriteAnimationState.SHAKING_HEAD],
}

# Default animation states to always consider (basic movement)
DEFAULT_ANIMATION_STATES = [
    SpriteAnimationState.SOUTH,
    SpriteAnimationState.FACE_NORTH,
    SpriteAnimationState.FACE_SOUTH,
]

# TODO: inc packet size by 1 for rooms with exp stars


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


def _create_empty_partition(
    ally_buffer: int, allow_extra: bool = True, extra_size: int = 1
) -> Partition:
    """Create a partition with all empty buffers."""
    return Partition(
        ally_sprite_buffer_size=ally_buffer,
        allow_extra_sprite_buffer=allow_extra,
        extra_sprite_buffer_size=extra_size if allow_extra else 0,
        buffers=[
            Buffer(BufferType.EMPTY_3, BufferSpace.BYTES_0, True),
            Buffer(BufferType.EMPTY_3, BufferSpace.BYTES_0, True),
            Buffer(BufferType.EMPTY_3, BufferSpace.BYTES_0, True),
        ],
        full_palette_buffer=True,
    )


def _get_complete_sprite(world: GameWorld, sprite_id: int) -> CompleteSprite | None:
    """Get CompleteSprite object for a given sprite ID.

    Uses world.get_sprite() pattern from physical_objects.py which provides
    direct access to animation properties via sprite.animation.properties.
    """
    try:
        return world.get_sprite(sprite_id)
    except (IndexError, AssertionError):
        return None


def _get_npc_sprite_id(obj: RoomObject | Clone) -> int:
    """Extract sprite ID from a room object."""
    return int(obj._npc.sprite_id)


def _npc_cannot_clone(obj: RoomObject | Clone) -> bool:
    """Check if an NPC cannot be cloned."""
    return bool(obj._npc.cannot_clone)


def _get_room_objects_with_clones(room: Room) -> list:  # type: ignore[type-arg]
    """Get all objects including expanded clones from a room.

    Note: Clone objects appear directly in room.objects as separate
    BattlePackClone, RegularClone, or ChestClone instances, not as
    an attribute on parent NPCs.
    """
    # Simply return all objects - clones are already in the list
    return list(room.objects)


def _room_contains_frog_coin_chests(world: GameWorld, room_index: int) -> bool:
    """Check if a room contains treasure chest locations with frog coin prizes.

    Args:
        world: The GameWorld instance containing locations
        room_index: The room index to check

    Returns:
        True if the room has any TreasureChestLocation with a FrogCoinPrize
    """
    for location in world.locations.values():
        if isinstance(location, TreasureChestLocation):
            if room_index in location._rooms:
                if location.prize is not None and isinstance(location.prize, FrogCoinPrize):
                    return True
    return False


# =============================================================================
# VRAM Calculation Functions
# Adapted from physical_objects.py NPC methods (min_vram_from_mold, etc.)
# =============================================================================


def _min_vram_from_mold(complete_sprite: CompleteSprite, mold_id: int) -> int:
    """Calculate min VRAM size from a specific mold.

    Based on physical_objects.py NPC.min_vram_from_mold().
    Formula: ceil(max(0, len(tiles) - 4) / 4)
    """
    molds = complete_sprite.animation.properties.molds
    if mold_id >= len(molds):
        return 0
    tiles = molds[mold_id].tiles
    return ceil(max(0, len(tiles) - 4) / 4)


def _min_vram_from_sequence(complete_sprite: CompleteSprite, sequence_id: int) -> int:
    """Calculate min VRAM size from a sequence (max across all frames/molds).

    Based on physical_objects.py NPC.min_vram_from_sequence().
    Iterates through all frames in the sequence and returns the maximum
    VRAM requirement across all referenced molds.
    """
    sequences = complete_sprite.animation.properties.sequences
    if sequence_id >= len(sequences):
        return 0

    min_vram = 0
    frames = sequences[sequence_id].frames
    for frame in frames:
        min_vram = max(min_vram, _min_vram_from_mold(complete_sprite, frame.mold_id))
    return min_vram


def _min_vram_from_script_contents(
    world: GameWorld, base_sprite_id: int, script_contents: list
) -> int:
    """Calculate min VRAM size from action script contents.

    Based on physical_objects.py NPC._min_vram_size_from_script().
    Parses SetSpriteSequence commands to find all molds/sequences used.
    """
    complete_sprite = _get_complete_sprite(world, base_sprite_id)
    if complete_sprite is None:
        return 0

    min_vram = _min_vram_from_mold(complete_sprite, 0)

    for cmd in script_contents:
        if isinstance(cmd, SetSpriteSequence):
            prop_id = cmd.index
            offset = cmd.sprite_offset

            # Get the sprite with offset applied
            offset_sprite = _get_complete_sprite(world, base_sprite_id + offset)
            if offset_sprite is None:
                continue

            if cmd.is_mold:
                min_vram = max(min_vram, _min_vram_from_mold(offset_sprite, prop_id))
            else:
                min_vram = max(
                    min_vram, _min_vram_from_sequence(offset_sprite, prop_id)
                )

    return min_vram


def _min_vram_from_action_script(
    world: GameWorld, base_sprite_id: int, script_id: int
) -> int:
    """Calculate min VRAM size from an action script.

    Based on physical_objects.py NPC.min_vram_from_action_script().
    """
    if script_id >= len(world.action_scripts.scripts):
        return 0

    script = world.action_scripts.scripts[script_id]
    if script is None:
        return 0

    return _min_vram_from_script_contents(world, base_sprite_id, script.contents)


def _min_vram_from_event_script(
    world: GameWorld, base_sprite_id: int, target: int, script_id: int
) -> int:
    """Calculate min VRAM size from event script subscripts targeting this NPC.

    Based on physical_objects.py NPC.min_vram_from_event_script().
    Parses the event script for ActionSubcriptCommandPrototype commands
    that target this NPC and calculates VRAM from their subscript contents.
    """
    complete_sprite = _get_complete_sprite(world, base_sprite_id)
    if complete_sprite is None:
        return 0

    min_vram = _min_vram_from_mold(complete_sprite, 0)

    try:
        script = world.event_scripts.get_script_by_id(script_id)
    except (KeyError, IndexError):
        return min_vram

    if script is None:
        return min_vram

    for cmd in script.contents:
        if isinstance(cmd, ActionSubcriptCommandPrototype) and cmd.target == target:
            min_vram = max(
                min_vram,
                _min_vram_from_script_contents(
                    world, base_sprite_id, cmd.subscript.contents
                ),
            )

    return min_vram


def _calculate_npc_min_vram(
    world: GameWorld, obj: RoomObject | Clone, obj_index: int
) -> int:
    """Calculate the min VRAM size an NPC needs based on its scripts.

    Checks both the NPC's action script and event script (if applicable)
    to determine the maximum VRAM requirement across all animations
    the NPC is expected to perform.
    """
    sprite_id = _get_npc_sprite_id(obj)
    min_vram = int(obj._npc.min_vram_size)

    # Check action script
    action_script_id = int(obj.action_script)
    if action_script_id > 0:
        action_vram = _min_vram_from_action_script(world, sprite_id, action_script_id)
        min_vram = max(min_vram, action_vram)

    # Check event script for NPCs that have one (RegularNPC, ChestNPC, RegularClone)
    if isinstance(obj, (RegularNPC, ChestNPC, RegularClone)):
        event_script_id = int(obj.event_script)
        if event_script_id > 0:
            # Target is the NPC's index in the room (plus NPC_0 offset)
            from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
                NPC_0,
            )

            target = NPC_0 + obj_index
            event_vram = _min_vram_from_event_script(
                world, sprite_id, target, event_script_id
            )
            min_vram = max(min_vram, event_vram)

    return min(min_vram, 7)  # Cap at 7 (max allowed value)


def update_npc_vram_sizes(world: GameWorld) -> None:
    """Update NPC min_vram_size values based on their expected animations.

    For each room, calculates what VRAM each NPC needs based on its
    action script and event script, then updates the NPC's min_vram_size
    if the calculated value is higher than the current value.

    This should be called before partition calculation to ensure NPCs
    have appropriate VRAM allocations for their animations.
    """
    for room_index in range(512):
        room = world.rooms._rooms[room_index]
        if room is None:
            continue

        for obj_index, obj in enumerate(room.objects):
            calculated_vram = _calculate_npc_min_vram(world, obj, obj_index)
            current_vram = int(obj._npc.min_vram_size)

            if calculated_vram > current_vram:
                # Update the NPC's min_vram_size
                obj._npc._min_vram_size = calculated_vram


# =============================================================================
# Ally Buffer Calculation
# Determines VRAM needed for player character based on room's extra_sprite_actions
# =============================================================================


def _calculate_ally_buffer_from_tile_count(tile_count: int) -> int:
    """Calculate ally buffer size from tile count.

    Formula: ceil(max(0, tile_count - 4) / 4), capped at 3.
    """
    return min(3, ceil(max(0, tile_count - 4) / 4))


def _get_ally_tile_count_for_state(ally: Ally, state: SpriteAnimationState) -> int:
    """Get the tile count for a specific animation state from the ally's sprite data.

    Checks _sprites_primary first, falls back to _sprites_secondary.
    Returns 0 if the state is not found.
    """
    # Tuple format: (mold_id, tile_count, is_primary)
    if state in ally._sprites_primary:
        return ally._sprites_primary[state][1]
    return 0


def calculate_ally_buffer_for_room(ally: Ally, room: Room, room_index: int | None = None) -> int:  # type: ignore[type-arg]
    """Calculate the ally buffer size needed for a specific room.

    Based on the room's extra_sprite_actions, determines which animation
    states the ally might need to perform, then calculates the maximum
    VRAM requirement across all those states.

    Args:
        ally: The overworld character (Ally instance with _sprites_primary/_sprites_secondary)
        room: The room to calculate for (with extra_sprite_actions list)
        room_index: Optional room index for debug output

    Returns:
        Ally buffer size (0-3)
    """
    # Start with default animation states (basic movement)
    states_to_check: set[SpriteAnimationState] = set(DEFAULT_ANIMATION_STATES)

    # Add states required by room's extra_sprite_actions
    for action in room.extra_sprite_actions:
        if action in EXTRA_ACTION_TO_ANIMATION_STATE:
            states_to_check.update(EXTRA_ACTION_TO_ANIMATION_STATE[action])

    # Find max tile count across all required states
    max_tile_count = 0
    max_state = None
    for state in states_to_check:
        tile_count = _get_ally_tile_count_for_state(ally, state)
        if tile_count > max_tile_count:
            max_tile_count = tile_count
            max_state = state

    buffer_size = _calculate_ally_buffer_from_tile_count(max_tile_count)

    return buffer_size


def set_partitions(world: GameWorld) -> None:
    """Calculate and set optimal partitions for all rooms in the world.

    This should be called after the shuffler has run, so that chest contents
    and NPC models are finalized.

    This function:
    1. Updates NPC min_vram_size values based on their action/event scripts
    2. Calculates optimal partition buffer configurations for each room
    3. Sets partition properties (ally buffer, extra sprite buffer, etc.)

    Args:
        world: The GameWorld instance containing rooms, sprites, and locations
    """
    # First, update NPC VRAM sizes based on their expected animations
    update_npc_vram_sizes(world)

    # Get the overworld character for ally buffer calculation
    # The ally buffer is calculated per-room based on what animations
    # the character might need to perform (from room's extra_sprite_actions)
    overworld_ally = world.overworld_character.ally

    # Process each room
    for room_index in range(512):
        room = world.rooms._rooms[room_index]

        if room is None:
            continue

        # Skip room 68 (special case)
        if room_index == R068_MIDAS_RIVER_BARREL_JUMPING_RIVER:
            continue

        # Calculate ally buffer for this specific room
        ally_buffer = calculate_ally_buffer_for_room(overworld_ally, room, room_index)  # type: ignore[arg-type]

        # Rooms that always need triple empty + extra 1
        if room_index in TRIPLE_EMPTY_EX1_ROOMS or len(room.objects) == 0:
            room.set_partition(_create_empty_partition(ally_buffer, True, 1))
            continue

        # Rooms that always need triple empty + extra 0
        if room_index in TRIPLE_EMPTY_EX0_ROOMS:
            room.set_partition(_create_empty_partition(ally_buffer, False, 0))
            continue

        # For rooms with objects, calculate the optimal partition
        if len(room.objects) > 0:
            original_partition = room.partition
            original_partition_copy = None
            if original_partition is not None:
                # Deep copy the original partition settings
                original_partition_copy = copy.deepcopy(original_partition)

            # Start with a base partition
            partition = Partition(
                ally_sprite_buffer_size=ally_buffer,
                allow_extra_sprite_buffer=False,
                extra_sprite_buffer_size=0,
                buffers=[
                    Buffer(BufferType.EMPTY_3, BufferSpace.BYTES_0, True),
                    Buffer(BufferType.EMPTY_3, BufferSpace.BYTES_0, True),
                    Buffer(BufferType.EMPTY_3, BufferSpace.BYTES_0, True),
                ],
                full_palette_buffer=True,
            )

            # Preserve some original partition settings if available
            if original_partition_copy is not None:
                partition.set_extra_sprite_buffer_size(
                    int(original_partition_copy.extra_sprite_buffer_size)
                )
                partition.set_allow_extra_sprite_buffer(
                    original_partition_copy.allow_extra_sprite_buffer
                )
                partition.set_full_palette_buffer(
                    original_partition_copy.full_palette_buffer
                )

            packet_size = int(partition.extra_sprite_buffer_size)
            if partition.allow_extra_sprite_buffer:
                packet_size += 1

            priority_buffers = []
            npc_buffers = []
            packet_buffers = []

            if room_index in SPECIAL_CASE_ROOMS:
                priority_buffers.append(BufferType.EMPTY_3)

            # Count non-coin ChestNPC objects in the room
            # When items pop out of chests (mushrooms, flowers, etc.), they need extra sprite buffer
            # Coin-only chests don't need this as coins use a different buffer type
            has_non_coin_chest = False
            for obj in room.objects:
                if isinstance(obj, (ChestNPC, ChestClone)):
                    sprite_id = _get_npc_sprite_id(obj)
                    # If the chest sprite is the regular treasure chest (not a coin), count it
                    if sprite_id == SPR0094_TREASURE_CHEST:
                        has_non_coin_chest = True
                        break

            # Set extra sprite buffer for chest items
            # Most rooms only need buffer=1 for chest packet sprites
            # Specific rooms with closely-spaced chests need higher values (defined in CLOSE_CHEST_ROOMS)
            if has_non_coin_chest:
                if room_index in CLOSE_CHEST_ROOMS:
                    packet_size = max(packet_size, CLOSE_CHEST_ROOMS[room_index])
                else:
                    packet_size = max(packet_size, 1)

            # Process NPCs for buffer requirements
            last_sprite = -1
            existing_formats_in_room = []
            decloned = _get_room_objects_with_clones(room)  # type: ignore[arg-type]

            for obj in decloned:
                sprite_id = _get_npc_sprite_id(obj)

                # Process sprites that CAN be cloned (sprite_id < 575 and not cannot_clone)
                if sprite_id < 575 and not _npc_cannot_clone(obj):
                    complete_sprite = _get_complete_sprite(world, sprite_id)
                    if complete_sprite is None:
                        continue

                    # Handle ally sprites (0-30)
                    if sprite_id <= SPR0034_GENO_MORPH_INTO_CANNON:
                        if room_index in [
                            R203_MUSHROOM_WAY_AREA_01,
                            R204_MUSHROOM_WAY_AREA_02,
                            R205_MUSHROOM_WAY_AREA_03,
                        ]:
                            # Skip for these rooms
                            continue
                        elif room_index == R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09:
                            if sprite_id < 7:
                                packet_size = max(4, packet_size)
                            else:
                                packet_size = max(3, packet_size)

                    # Check for special sprite types
                    if sprite_id == SPR0094_TREASURE_CHEST:
                        priority_buffers.append(BufferType.TREASURE_CHEST)
                    elif sprite_id in [
                        SPR0192_COIN,
                        SPR0193_SMALL_COIN,
                        SPR0194_FROG_COIN,
                        SPR0606_SMALL_FROG_COIN,
                    ]:
                        priority_buffers.append(BufferType.COINS)

                    # Determine buffer type based on animation properties
                    # Uses CompleteSprite.animation.properties pattern from physical_objects.py
                    molds = complete_sprite.animation.properties.molds
                    if molds and len(molds) > 0:
                        mold = molds[0]
                        if not mold.gridplane:
                            priority_buffers.append(BufferType.EMPTY_3)
                        elif mold.tiles and len(mold.tiles) > 0:
                            tile = mold.tiles[0]
                            # All Tile types (Tile, GridplaneArrangement, NonGridplaneArrangement) have format
                            tile_format = tile.format  # type: ignore[attr-defined]
                            if tile_format <= 1:
                                buf = BufferType.FOUR_SPRITES_PER_ROW
                            else:
                                buf = BufferType.THREE_SPRITES_PER_ROW

                            if buf not in existing_formats_in_room:
                                existing_formats_in_room.append(buf)
                                # Clone objects are separate instances in room.objects, not attributes
                                if isinstance(obj, (BattlePackClone, RegularClone, ChestClone)):
                                    npc_buffers.append(buf)
                            elif sprite_id != last_sprite:
                                npc_buffers.append(buf)
                            elif len(npc_buffers) == 0 or npc_buffers[-1] != buf:
                                npc_buffers.append(buf)

                    last_sprite = sprite_id

            # Remove duplicates while preserving order
            priority_buffers = list_unique(priority_buffers)
            packet_buffers = list_unique(packet_buffers)

            # Special cases for specific rooms
            if room_index in [56, 57, 58]:
                npc_buffers.insert(0, BufferType.FOUR_SPRITES_PER_ROW)
            elif room_index == 301:
                npc_buffers.append(BufferType.THREE_SPRITES_PER_ROW)

            # Handle coin buffer requirements
            if room_index in ALWAYS_REQUIRES_COIN_BUFFER:
                if BufferType.COINS not in packet_buffers:
                    packet_buffers.append(BufferType.COINS)

            # Check if room contains frog coin chests (need COINS buffer for frog coin sprites)
            if _room_contains_frog_coin_chests(world, room_index):
                if BufferType.COINS not in packet_buffers:
                    packet_buffers.append(BufferType.COINS)

            # Avoid duplicate coin buffers
            if (
                BufferType.COINS in priority_buffers
                and BufferType.COINS in packet_buffers
            ):
                priority_buffers.remove(BufferType.COINS)

            # Assign final buffer configuration
            final_buffers: list[BufferType | None] = [None, None, None]
            buffers = priority_buffers + npc_buffers + packet_buffers

            # Treasure chest goes in slot 0 if present
            if BufferType.TREASURE_CHEST in buffers:
                final_buffers[0] = BufferType.TREASURE_CHEST
                buffers.remove(BufferType.TREASURE_CHEST)
            elif BufferType.EMPTY_3 in priority_buffers:
                final_buffers[0] = BufferType.EMPTY_3
                buffers.remove(BufferType.EMPTY_3)

            # Coins go in slot 2 if present
            if BufferType.COINS in buffers:
                final_buffers[2] = BufferType.COINS
                buffers.remove(BufferType.COINS)

            # Fill remaining slots
            idx = 0
            for i in range(3):
                if final_buffers[i] is None and idx < len(buffers):
                    final_buffers[i] = buffers[idx]
                    idx += 1

            # Fill any remaining None slots with EMPTY_3
            for i in range(3):
                if final_buffers[i] is None:
                    final_buffers[i] = BufferType.EMPTY_3

            # Apply buffer types to partition
            partition_buffers = partition.buffers
            found = False
            for i, buf_type in enumerate(final_buffers):
                assert buf_type is not None  # Guaranteed by the None-filling loop above
                partition_buffers[i].set_buffer_type(buf_type)
                # Try to preserve original buffer space settings if they match
                if original_partition_copy is not None and not found:
                    for orig_buf in original_partition_copy.buffers:
                        if orig_buf.buffer_type == buf_type and int(
                            orig_buf.main_buffer_space
                        ) > int(partition_buffers[i].main_buffer_space):
                            partition_buffers[i].set_main_buffer_space(
                                orig_buf.main_buffer_space
                            )
                            partition_buffers[i].set_index_in_main_buffer(
                                orig_buf.index_in_main_buffer
                            )
                            found = True
                            break

            partition.set_ally_sprite_buffer_size(ally_buffer)

            if packet_size > 0:
                partition.set_allow_extra_sprite_buffer(True)
                partition.set_extra_sprite_buffer_size(packet_size - 1)
            else:
                partition.set_allow_extra_sprite_buffer(False)
                partition.set_extra_sprite_buffer_size(0)

            room.set_partition(partition)
