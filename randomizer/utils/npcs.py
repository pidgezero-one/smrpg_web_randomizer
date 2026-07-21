"""Utils for NPCs"""

from __future__ import annotations
from math import ceil
from typing import TYPE_CHECKING

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, Mold, Tile
from smrpgpatchbuilder.datatypes.levels.classes import NPC, VramStore
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import SOUTHWEST
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import NPC_0
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import AreaObject, Direction
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import ActionQueueSync, Pause
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import A_SetSpriteSequence, A_Pause

from ..types.physical_objects import BossNPC

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


def min_vram_from_mold_geometry(mold: Mold, player_sprite: bool = False) -> int:
    """The min_vram_size a single mold requires. Canonical VRAM sizing rule.

    The engine hands a cannot_clone NPC `4 * (min_vram_size + 1)` 16x16 tile
    slots ($C0:8EBC, where $66 is the NPC record's 3-bit vram field already
    multiplied by 4 at $C0:8CF3). A slot holds four 8x8 subtiles, so capacity is
    `16 * (min_vram_size + 1)` subtiles and the baseline is 16.

    Two render paths pack that capacity differently, so `player_sprite` selects
    the unit:

    - NPC clone/dedicated path (default): packs only the subtiles a tile actually
      carries. A mold tile's presence bitmask (ROM byte0 bits 7-4) marks which of
      its four 8x8 quadrants exist; absent ones occupy no VRAM. Vanilla pins this:
      sprite 48 ships as CROCO_NPC_2 (min_vram 0, plays only sequence 5, max 14
      subtiles) and CROCO_NPC (min_vram 1, sequences 4/6, max 18 subtiles);
      Yaridovich (40 subtiles) ships min_vram 2. Sequence 5's mold 17 has five
      tiles but only 14 subtiles — counting tiles inflates it to 1 and overruns
      room 206's cursor into the treasure-chest buffer.

    - Protagonist path (`player_sprite=True`): the active character renders through
      VramStore 7's SA-1 bulk-DMA path, which uploads whole 16x16 tiles — every
      tile reserves all four quadrants whether or not they're populated. Peach's
      DOWN_PIPE pose (sprite 964 mold 30) is 7 tiles but only 14 present subtiles;
      packed it would read as 0, but in-game it overflows a size-1 ally buffer and
      the save-point NPC overwrites her. 7 tiles reserve 28 subtiles -> 2 units.
    """
    if mold.gridplane:
        return 0
    tiles = [tile for tile in mold.tiles if isinstance(tile, Tile)]
    if player_sprite:
        reserved = 4 * len(tiles)
    else:
        reserved = sum(
            1 for tile in tiles for subtile in tile.subtile_bytes if subtile is not None
        )
    return ceil(max(0, reserved - 16) / 16)


def min_vram_from_sequence_for_sprite(
    world: "GameWorld", sprite_id: int, sequence_id: int, player_sprite: bool = False
) -> int:
    """Compute min_vram_from_sequence for a given sprite ID and sequence.

    This is a standalone version of NPC.min_vram_from_sequence that works
    from a sprite_id rather than requiring an NPC instance. Pass
    `player_sprite=True` when sizing the protagonist's ally buffer — see
    min_vram_from_mold_geometry.
    """
    sprite = world.get_sprite(sprite_id)
    assert sequence_id < len(sprite.animation.properties.sequences)
    molds = sprite.animation.properties.molds
    return max(
        (
            min_vram_from_mold_geometry(molds[frame.mold_id], player_sprite)
            for frame in sprite.animation.properties.sequences[sequence_id].frames
        ),
        default=0,
    )


def min_vram_from_mold_for_sprite(
    world: "GameWorld", sprite_id: int, mold_id: int, player_sprite: bool = False
) -> int:
    """Compute min_vram_from_mold for a given sprite ID and mold ID.

    Standalone version of NPC.min_vram_from_mold — works from a sprite_id
    rather than requiring an NPC instance. Returns 0 if mold_id is out of range.
    Pass `player_sprite=True` when sizing the protagonist's ally buffer.
    """
    sprite = world.get_sprite(sprite_id)
    molds = sprite.animation.properties.molds
    if mold_id >= len(molds):
        return 0
    return min_vram_from_mold_geometry(molds[mold_id], player_sprite)


# Per-character protagonist sprite base IDs.
#
# When the engine renders the active protagonist, it uses:
#   - Mario protagonist (ally.index=0): sprite 0 (SPR0000_MARIO_WALKING_DOWN_LEFT — the
#     real protagonist sprite, NOT the Mario clone monster sprite at SPR0409 used by
#     MarioCharacterNPC._base).
#   - Any non-Mario protagonist (ally.index 1-4): sprite 31 (SPR0031_ALT_PROTAGONIST_1)
#     after the per-character protagonist remap fills sprites 31-37 with that
#     character's protagonist data via apply.py / cosmetics.py.
#
# This is what `update_partition_by_protagonist` and `_calculate_ally_buffer_size` should
# use for VRAM calculations — NOT character_model.base.sprite_id, which points at the
# per-character non-protagonist sprite (sprite 7 for Toadstool, sprite 13 for Bowser, etc.)
# or at the Mario clone monster sprite (sprite 409). Those are placeholders for when the
# character appears as an NPC, not for partition sizing.
PROTAGONIST_BASE_SPRITE_ID: dict[int, int] = {
    0: 0,    # Mario   — SPR0000_MARIO_WALKING_DOWN_LEFT
    1: 31,   # Toadstool — SPR0031_ALT_PROTAGONIST_1 (post-remap with TOADSTOOL_962-968)
    2: 31,   # Bowser    — SPR0031_ALT_PROTAGONIST_1 (post-remap with BOWSER_969-975)
    3: 31,   # Geno      — SPR0031_ALT_PROTAGONIST_1 (post-remap with GENO_983-989)
    4: 31,   # Mallow    — SPR0031_ALT_PROTAGONIST_1 (post-remap with MALLOW_976-982)
}

# The protagonist sprite range is 7 sprites (offsets 0-6 from the base). Offsets >= 7
# in the per-ally `_sprites_primary` dicts reference NON-protagonist sprites — typically
# extended NPC sprites that the engine references in specific cutscene contexts, not
# protagonist animations. They should NOT contribute to partition VRAM sizing because
# they aren't loaded into the protagonist sprite slot.
PROTAGONIST_SPRITE_RANGE = 7  # offsets 0..6 valid


def get_protagonist_sprite(world: "GameWorld", ally_index: int, offset: int):
    """Return the sprite at `protagonist_base + offset`, but only if it's actually
    within the protagonist sprite range. Returns None for offsets outside the range
    (those refer to unrelated sprites that shouldn't contribute to partition calc).

    This goes through `world.get_sprite()`, so for non-Mario protagonists it will
    return the post-remap protagonist sprite — but ONLY if cosmetics.py has already
    written sprites 31-37 by the time this is called. Callers that need to run
    before that remap should pass through this helper *after* the remap, or the
    sprite data will be the default empty placeholder.
    """
    if offset >= PROTAGONIST_SPRITE_RANGE:
        return None
    if ally_index not in PROTAGONIST_BASE_SPRITE_ID:
        return None
    base = PROTAGONIST_BASE_SPRITE_ID[ally_index]
    try:
        return world.get_sprite(base + offset)
    except (IndexError, AssertionError):
        return None


def is_swse_only(sprite: CompleteSprite):
    sequences = sprite.animation.properties.sequences
    if len(sequences) < 2:
        return True
    south = sequences[0]
    north = sequences[1]
    if len(north.frames) != len(south.frames):
        return False
    for comp1, comp2 in zip(south.frames, north.frames):
        if comp1.mold_id != comp2.mold_id:
            return False
    return True


def set_npc_direction_if_swse_only(
    world: GameWorld,
    room_id: int,
    npc_id: AreaObject,
    npc_base: NPC,
    direction: Direction = SOUTHWEST,
) -> None:
    """Set an NPC's direction to SOUTHWEST if its sprite only has SW/SE directions.

    This is useful when swapping NPCs with sprites that only support south-facing
    directions, ensuring they don't display incorrectly when facing north.

    Args:
        world: The game world.
        room_id: The room ID where the NPC is located.
        npc_id: The NPC's target ID within the room.
        npc_base: The NPC base model to check for direction constraints.
    """
    room = world.rooms._rooms[room_id]
    assert room is not None
    obj = room.get_npc_by_target_id(npc_id)
    if obj is not None:
        sprite = world.sprites.sprites[npc_base.sprite_id]
        if npc_base.directions == VramStore.DIR2_SWSE or is_swse_only(sprite):
            obj.set_direction(direction)


def set_mines_punch_command(world: GameWorld, boss: BossNPC):
    contact_frame = 1  # Default to 1 (minimum valid pause duration)
    if boss.animations is None or boss.animations.mines_punch is None:
        world.event_scripts.delete_command_by_identifier("inner_mines_boss_shove_animation")
    else:
        collection = boss.animations.mines_punch
        contact_frame = collection.contact_frame or 12  # Ensure at least 1
        boss_pause_length = collection.total_duration
        boss_animation = ActionQueueSync(target=NPC_0, subscript=[
            A_SetSpriteSequence(index=collection.sequence_id, is_sequence=True, looping=False),
            A_Pause(boss_pause_length),
        ])
        world.event_scripts.replace_command_by_identifier("inner_mines_boss_shove_animation", boss_animation)
    world.event_scripts.replace_subscript_command_by_identifier(
        "inner_mines_mario_shoved_backward",
        "inner_mines_mario_shoved_backward_duration",
        A_Pause(contact_frame)
    )
    world.event_scripts.get_command_by_identifier("inner_mines_mario_shoved_backward_pause", Pause).set_length(contact_frame)
        