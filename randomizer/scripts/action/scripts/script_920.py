"""A0920_STATIC_DRY_BONES_COLLAPSE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        PlaySound(sound=SO117_SPINNING_MONSTER, channel=4),
        Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F, pixel=True),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 7, ["ACTION_920_set_sprite_sequence_14"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 1, ["ACTION_920_set_sprite_sequence_14"]
        ),
        SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        ClearSolidityBits(bit_4=True, cant_walk_through=True),
        Pause(240),
        PlaySound(sound=SO117_SPINNING_MONSTER, channel=4),
        SetSpriteSequence(index=8, looping=False),
        Pause(36),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        SetSolidityBits(bit_4=True, cant_walk_through=True),
        Return(),
        SetSpriteSequence(
            index=6,
            is_mold=True,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_920_set_sprite_sequence_14"),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        ClearSolidityBits(bit_4=True, cant_walk_through=True),
        Pause(120),
        SetSpriteSequence(index=8, looping=False, mirror_sprite=True),
        Pause(36),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        SetSolidityBits(bit_4=True, cant_walk_through=True),
        Return(),
    ]
)
