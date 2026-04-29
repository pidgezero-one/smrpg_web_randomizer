"""Utils for NPCs"""

from __future__ import annotations
from math import ceil
from typing import TYPE_CHECKING

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, Tile
from smrpgpatchbuilder.datatypes.levels.classes import NPC, VramStore
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import SOUTHWEST
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import NPC_0
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import AreaObject, Direction
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import ActionQueueSync
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands.commands import A_SetSpriteSequence, A_Pause

from ..types.physical_objects import BossNPC

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld


def min_vram_from_sequence_for_sprite(world: "GameWorld", sprite_id: int, sequence_id: int) -> int:
    """Compute min_vram_from_sequence for a given sprite ID and sequence.

    This is a standalone version of NPC.min_vram_from_sequence that works
    from a sprite_id rather than requiring an NPC instance.
    """
    sprite = world.get_sprite(sprite_id)
    assert sequence_id < len(sprite.animation.properties.sequences)
    min_vram = 0
    for frame in sprite.animation.properties.sequences[sequence_id].frames:
        mold = sprite.animation.properties.molds[frame.mold_id]
        if mold.gridplane:
            continue
        truthy_subtiles = 0
        for t in mold.tiles:
            if isinstance(t, Tile):
                truthy_subtiles += len([s for s in t.subtile_bytes if s is not None])
        min_vram = max(min_vram, ceil(max(0, truthy_subtiles - 16) / 16))
    return min_vram


def min_vram_from_mold_for_sprite(world: "GameWorld", sprite_id: int, mold_id: int) -> int:
    """Compute min_vram_from_mold for a given sprite ID and mold ID.

    Standalone version of NPC.min_vram_from_mold — works from a sprite_id
    rather than requiring an NPC instance. Returns 0 for gridplane molds
    or if mold_id is out of range.
    """
    sprite = world.get_sprite(sprite_id)
    if mold_id >= len(sprite.animation.properties.molds):
        return 0
    mold = sprite.animation.properties.molds[mold_id]
    if mold.gridplane:
        return 0
    truthy_subtiles = 0
    for t in mold.tiles:
        if isinstance(t, Tile):
            truthy_subtiles += len([s for s in t.subtile_bytes if s is not None])
    return ceil(max(0, truthy_subtiles - 16) / 16)


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
        contact_frame = max(1, collection.contact_frame or 1)  # Ensure at least 1
        sequence_id = collection.sequence_id
        sprite_id = boss.base.sprite_id
        sprite = world.sprites.sprites[sprite_id]
        num_sequences = len(sprite.animation.properties.sequences)
        assert sequence_id < num_sequences, (
            f"Mines punch animation error: {boss.__class__.__name__} references "
            f"sequence {sequence_id} but sprite {sprite_id} only has {num_sequences} sequences"
        )
        sequence = sprite.animation.properties.sequences[sequence_id]
        boss_pause_length = sequence.total_duration
        try:
            
            final_mold = sequence.frames[-1].mold_id
        except IndexError:
            raise Exception(
                f"Mines punch animation error: {boss.__class__.__name__} references "
                f"sequence {sequence_id} has {len(sequence.frames)} frames"
            )
        boss_animation = ActionQueueSync(target=NPC_0, subscript=[
            A_SetSpriteSequence(index=sequence_id, is_sequence=True, looping=False),
            A_Pause(boss_pause_length),
            A_SetSpriteSequence(index=final_mold, is_mold=True, is_sequence=True, looping=True)
        ])
        world.event_scripts.replace_command_by_identifier("inner_mines_boss_shove_animation", boss_animation)
    world.event_scripts.replace_subscript_command_by_identifier(
        "inner_mines_mario_shoved_backward",
        "inner_mines_mario_shoved_backward_duration",
        A_Pause(contact_frame)
    )
        