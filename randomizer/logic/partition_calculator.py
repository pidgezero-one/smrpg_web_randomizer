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
from dataclasses import dataclass

from smrpgpatchbuilder.datatypes.overworld_scripts.arguments import NPC_13, NPC_6
from ..data.variables.sprite_names import *
from ..data.variables.room_names import *

from smrpgpatchbuilder.datatypes.levels.classes import (
    BufferSpace,
    BufferType,
)
from ..types.ally import SpriteAnimationState
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (
    NPC_0,
    NPC_1,
    NPC_2,
    NPC_3,
    NPC_4,
    NPC_7,
    NPC_8
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


def _buffer_by_sprite_format(world: GameWorld, sprite_id: int) -> BufferType:
    """Determine buffer type needed for a given sprite ID based on its gridplane format."""
    is_gridplane, format = _get_npc_gridplane_info(world, sprite_id)
    if is_gridplane:
        if format in [0, 1]:
            return BufferType.FOUR_SPRITES_PER_ROW
        elif format in [2, 3]:
            return BufferType.THREE_SPRITES_PER_ROW
    return BufferType.EMPTY_3


def _buffer_by_room_object(world: GameWorld, npc: RoomObject) -> BufferType:
    """Determine buffer type needed for a given NPC based on its sprite."""
    sprite_id = npc._npc.sprite_id
    return _buffer_by_sprite_format(world, sprite_id)


def _update_buffer_by_room_object(
    world: GameWorld, room_id: int, npc: AreaObject, buffer_index: int, buffer_space: BufferSpace | None = None
) -> None:
    room = world.rooms._rooms[room_id]
    assert room is not None
    assert room.partition is not None
    npc_obj = room.get_npc_by_target_id(npc)
    room.partition.buffers[buffer_index].set_buffer_type(
        _buffer_by_room_object(world, npc_obj)
    )
    if buffer_space is not None:
        room.partition.buffers[buffer_index].set_main_buffer_space(buffer_space)


def update_statue_room_partitions(world: GameWorld) -> None:
    _update_buffer_by_room_object(world, R341_NIMBUS_LAND_GARROS_HOUSE, NPC_1, 1)
    _update_buffer_by_room_object(world, R110_NIMBUS_CASTLE_AREA_18_DODOS_STATUEPOLISHING_ROOM, NPC_0, 0)
    _update_buffer_by_room_object(world, R109_NIMBUS_CASTLE_AREA_01_ENTRANCE_HALL, NPC_0, 0)
    _update_buffer_by_room_object(world, R115_NIMBUS_CASTLE_AREA_03_4WAY_PATH_DURING_VALENTINA, NPC_0, 0)
    _update_buffer_by_room_object(world, R122_NIMBUS_CASTLE_AREA_12_ENTRANCE_TO_THRONE_ROOM, NPC_0, 1)
    _update_buffer_by_room_object(world, R120_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_DURING_VALENTINA, NPC_0, 1)
    _update_buffer_by_room_object(world, R113_NIMBUS_CASTLE_AREA_16_SMALL_TWODOOR_ROOM_WTREASURE_FROM_AREA_15, NPC_3, 2)
    _update_buffer_by_room_object(world, R119_NIMBUS_CASTLE_AREA_06_LEFTMOST_FRONT_DOOR_FROM_AREA_05, NPC_6, 2)
    _update_buffer_by_room_object(world, R408_NIMBUS_CASTLE_AREA_14_RIGHTMOST_FRONT_DOOR_OF_LONG_5EXIT_ROOM, NPC_6, 2)
    # Skip room 113, it has both a 3 and a 4 buffer. See what happens when there's a non gridplane enemy here
    _update_buffer_by_room_object(world, R440_NIMBUS_CASTLE_AREA_13_THRONE_ROOM_AFTER_VALENTINA, NPC_0, 1)
    _update_buffer_by_room_object(world, R447_NIMBUS_LAND_HOT_SPRINGS, NPC_1, 0)
    _update_buffer_by_room_object(world, R447_NIMBUS_LAND_HOT_SPRINGS, NPC_1, 1)
    _update_buffer_by_room_object(world, R447_NIMBUS_LAND_HOT_SPRINGS, NPC_1, 2)
    _update_buffer_by_room_object(world, R497_NIMBUS_CASTLE_AREA_06_DUMMY, NPC_0, 0)
    _update_buffer_by_room_object(world, R499_NIMBUS_CASTLE_AREA_05_LONG_5EXIT_ROOM_AFTER_VALENTINA, NPC_1, 1)
    _update_buffer_by_room_object(world, R501_NIMBUS_CASTLE_AREA_03_4WAY_PATH_AFTER_VALENTINA, NPC_0, 0)
    

def update_kitchen_partitions(world: GameWorld) -> None:
    _update_buffer_by_room_object(world, R155_MARRYMORE_CHAPEL_KITCHEN, NPC_0, 0)
    _update_buffer_by_room_object(world, R155_MARRYMORE_CHAPEL_KITCHEN, NPC_1, 1, BufferSpace.BYTES_512)
    _update_buffer_by_room_object(world, R155_MARRYMORE_CHAPEL_KITCHEN, NPC_2, 2, BufferSpace.BYTES_512)


def update_mines_henchman_room_partitions(world: GameWorld) -> None:
    """Update partition buffers for mines henchman rooms based on sprite width.

    Rooms 277 and 283 have henchman NPCs shuffled into them from OuterMinesBossFight.
    If the henchman sprite is 24px wide (gridplane format 0 or 1), the room's
    partition buffer needs to be set to FOUR_SPRITES_PER_ROW.

    - Room 277: Update first buffer (index 0)
    - Room 283: Update second buffer (index 1)

    This should be called after boss shuffling is complete.
    """

    # Room configurations: (room_index, buffer_index)
    room_configs = [
        (277, 1),  # Room 277: first buffer
        (283, 1),  # Room 283: second buffer
    ]

    for room_index, buffer_index in room_configs:
        _update_buffer_by_room_object(world, room_index, NPC_1, buffer_index)
    _update_buffer_by_room_object(world, R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM, NPC_0, 0)
    _update_buffer_by_room_object(world, R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM, NPC_0, 0)
    _update_buffer_by_room_object(world, R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM, NPC_0, 0)


def update_protagonist_room_partition(world: GameWorld) -> None:
    """Update room 284's first partition buffer based on the recruited character's sprite.

    If the character's sprite mold 0 is a gridplane with format 0 or 1 (24px wide),
    set the first buffer to FOUR_SPRITES_PER_ROW.
    If the mold is not a gridplane at all, set it to EMPTY_3.

    This should be called after character recruitment is determined.
    """
    PROTAGONIST_ROOM_INDEX = 284

    room = world.rooms._rooms[PROTAGONIST_ROOM_INDEX]
    assert room is not None, f"Room {PROTAGONIST_ROOM_INDEX} not found"
    assert room.partition is not None, f"Room {PROTAGONIST_ROOM_INDEX} has no partition"
    assert (
        len(room.partition.buffers) > 0
    ), f"Room {PROTAGONIST_ROOM_INDEX} has no partition buffers"

    # Get the recruited character's sprite
    character_model = world.overworld_character.character_model
    sprite_id = character_model._base.sprite_id
    complete_sprite = _get_complete_sprite(world, sprite_id)
    if complete_sprite is None:
        room.partition.buffers[0].set_buffer_type(BufferType.EMPTY_3)
        return

    # Check the first mold's gridplane format
    molds = complete_sprite.animation.properties.molds
    if not molds or len(molds) == 0:
        room.partition.buffers[0].set_buffer_type(BufferType.EMPTY_3)
        return

    first_mold = molds[0]
    if not first_mold.gridplane:
        # Non-gridplane - set to empty
        room.partition.buffers[0].set_buffer_type(BufferType.EMPTY_3)
        return

    if not first_mold.tiles or len(first_mold.tiles) == 0:
        room.partition.buffers[0].set_buffer_type(BufferType.EMPTY_3)
        return

    # Get the gridplane format from the first tile
    first_tile = first_mold.tiles[0]
    tile_format = first_tile.format  # type: ignore[attr-defined]

    # Set buffer based on format
    if tile_format in [0, 1]:
        room.partition.buffers[0].set_buffer_type(BufferType.FOUR_SPRITES_PER_ROW)

def update_johnny_room_partition(world: GameWorld) -> None:
    _update_buffer_by_room_object(world, R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM, NPC_0, 0)
    _update_buffer_by_room_object(world, R028_SUNKEN_SHIP_POSTKC_AREA_17_JOHNNYS_ROOM, NPC_1, 1)

def update_mushroom_kingdom_partitions(world: GameWorld) -> None:
    _update_buffer_by_room_object(world, R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL, NPC_0, 1)
    _update_buffer_by_room_object(world, R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, NPC_0, 0)
    _update_buffer_by_room_object(world, R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, NPC_3, 1)
    _update_buffer_by_room_object(world, R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F, NPC_1, 1)
    _update_buffer_by_room_object(world, R323_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_THRONE_ROOM, NPC_0, 0)
    _update_buffer_by_room_object(world, R323_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_THRONE_ROOM, NPC_1, 1)
    _update_buffer_by_room_object(world, R323_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_THRONE_ROOM, NPC_1, 2)
    _update_buffer_by_room_object(world, R329_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_BRANCH_ROOM_TO_VAULTGUEST_ROOM, NPC_0, 0)
    _update_buffer_by_room_object(world, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, NPC_0, 0)
    _update_buffer_by_room_object(world, R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM, NPC_1, 1)
    _update_buffer_by_room_object(world, R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM, NPC_0, 0)
    _update_buffer_by_room_object(world, R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM, NPC_4, 1)
    _update_buffer_by_room_object(world, R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM, NPC_8, 2)

def update_chapel_partition(world: GameWorld) -> None:
    _update_buffer_by_room_object(world, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, NPC_0, 0)
    _update_buffer_by_room_object(world, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, NPC_3, 1)
    _update_buffer_by_room_object(world, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, NPC_7, 2)

def update_arrow_partitions(world: GameWorld) -> None:
    _update_buffer_by_room_object(world, R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, NPC_7, 2)
    _update_buffer_by_room_object(world, R228_FOREST_MAZE_AREA_04, NPC_1, 2)
    _update_buffer_by_room_object(world, R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09, NPC_13, 2)
    
def update_mines_inner_henchman_room_partition(world: GameWorld) -> None:
    _update_buffer_by_room_object(world, R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, NPC_4, 1)
    _update_buffer_by_room_object(world, R289_MOLEVILLE_MINES_AREA_17_PUNCHINELLOS_ROOM_BEFORE_BATTLE, NPC_4, 2)

