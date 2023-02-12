from typing import List
from randomizer.types.npcs.objects.classes import NPC, AreaNPC, Coin
from math import ceil
from randomizer.types.overworld_scripts.action_scripts.classes import (
    ActionScriptCommand,
)
from randomizer.types.overworld_scripts.action_scripts.commands import SetSpriteSequence
from randomizer.types.overworld_scripts.event_scripts.classes import (
    ActionQueuePrototype,
    EventScript,
)
from randomizer.types.world.classes import GameWorld


def is_npc_equal(npc1: NPC, npc2: NPC):
    return (
        npc1.sprite_id == npc2.sprite_id
        and npc1.show_shadow == npc2.show_shadow
        and npc1.shadow_size == npc2.shadow_size
        and npc1.acute_axis == npc2.acute_axis
        and npc1.obtuse_axis == npc2.obtuse_axis
        and npc1.height == npc2.height
        and npc1.directions == npc2.directions
        and npc1.min_vram_size == npc2.min_vram_size
        and npc1.byte2_bit0 == npc2.byte2_bit0
        and npc1.byte2_bit1 == npc2.byte2_bit1
        and npc1.byte2_bit2 == npc2.byte2_bit2
        and npc1.byte2_bit3 == npc2.byte2_bit3
        and npc1.byte2_bit4 == npc2.byte2_bit4
        and npc1.byte5_bit6 == npc2.byte5_bit6
        and npc1.byte5_bit7 == npc2.byte5_bit7
        and npc1.byte6_bit2 == npc2.byte6_bit2
    )


def is_area_npc_equal(npc1: AreaNPC, npc2: AreaNPC):
    return (
        npc1.occupant.sprite_id == npc2.occupant.sprite_id
        and (
            (not npc1.show_shadow and not npc2.show_shadow)
            or (
                npc1.show_shadow
                and npc2.show_shadow
                and npc1.occupant.shadow_size == npc2.shadow_size
            )
        )
        and npc1.priority_0 == npc2.priority_0
        and npc1.priority_1 == npc2.priority_1
        and npc1.priority_2 == npc2.priority_2
        and npc1.occupant.y_shift == npc2.occupant.y_shift
        and npc1.acute_axis == npc2.acute_axis
        and npc1.obtuse_axis == npc2.obtuse_axis
        and npc1.height == npc2.height
        and npc1.directions == npc2.directions
        and npc1.vram_size == npc2.vram_size
        and npc1.cannot_clone == npc2.cannot_clone
        and npc1.occupant.sprite_id == npc2.occupant.sprite_id
        and npc1.occupant.byte2_bit0 == npc2.occupant.byte2_bit0
        and npc1.occupant.byte2_bit1 == npc2.occupant.byte2_bit1
        and npc1.occupant.byte2_bit2 == npc2.occupant.byte2_bit2
        and npc1.occupant.byte2_bit3 == npc2.occupant.byte2_bit3
        and npc1.occupant.byte2_bit4 == npc2.occupant.byte2_bit4
        and npc1.occupant.byte5_bit6 == npc2.occupant.byte5_bit6
        and npc1.occupant.byte5_bit7 == npc2.occupant.byte5_bit7
        and npc1.occupant.byte6_bit2 == npc2.occupant.byte6_bit2
    )


def min_vram(number_of_tiles: int):
    return ceil(max(0, number_of_tiles - 4) / 4)


# TODO: typing for this, need sprite data classes
def get_min_vram_from_mold(sprite, id):
    # print("mold:", sprite, id)
    tiles = sprite.animation.properties.molds[id].tiles
    return min_vram(len(tiles))


# TODO: typing for this, need sprite data classes
def get_min_vram_from_animation(sprite, id):
    min_vram = 0
    seq = sprite.animation.properties.sequences[id].frames
    # print("seq:", sprite, seq)
    for frame in seq:
        # print("frame:", frame)
        min_vram = max(min_vram, get_min_vram_from_mold(sprite, frame.mold_id))
    return min_vram


# TODO: typing for this, need sprite data classes
def get_min_vram_size_for_actionscript(
    world: GameWorld, sprite_id: int, subscript: List[ActionScriptCommand]
):
    min_vram = get_min_vram_from_mold(world.sprites[sprite_id], 0)
    for cmd in subscript:
        if isinstance(cmd, SetSpriteSequence):
            sequence = cmd.index
            offset = cmd.sprite_offset
            sprite = world.sprites[sequence + offset]
            if cmd.is_mold:
                min_vram = max(min_vram, get_min_vram_from_mold(sprite, sequence))
            else:
                min_vram = max(min_vram, get_min_vram_from_animation(sprite, sequence))
    return min_vram


def get_min_vram_size_for_eventscript(
    world: GameWorld, npc_id: int, sprite_id: int, script: EventScript
):
    min_vram: int = get_min_vram_from_mold(world.sprites[sprite_id], 0)
    for cmd in script.contents:
        if isinstance(cmd, ActionQueuePrototype) and cmd.target == npc_id + 0x14:
            min_vram = max(
                min_vram,
                get_min_vram_size_for_actionscript(
                    world, sprite_id, cmd.subscript.contents
                ),
            )
    return min_vram


def is_coin(model):
    return isinstance(model, Coin)
