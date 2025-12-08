"""A0408_JUMP_ON_SAVE_BLOCK"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 0, ["ACTION_408_set_sprite_sequence_10"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 1, ["ACTION_408_set_sprite_sequence_12"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 2, ["ACTION_408_set_sprite_sequence_14"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 3, ["ACTION_408_set_sprite_sequence_16"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 4, ["ACTION_408_set_sprite_sequence_18"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 5, ["ACTION_408_set_sprite_sequence_20"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 6, ["ACTION_408_set_sprite_sequence_22"]
        ),
        SetSpriteSequence(
            index=4,
            sprite_offset=1,
            is_mold=True,
            is_sequence=True,
            looping=True,
            mirror_sprite=True),
        Jmp(["ACTION_408_ret_23"]),
        SetSpriteSequence(
            index=2,
            sprite_offset=1,
            is_mold=True,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_408_set_sprite_sequence_10"),
        Jmp(["ACTION_408_ret_23"]),
        SetSpriteSequence(
            index=3,
            sprite_offset=1,
            is_mold=True,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_408_set_sprite_sequence_12"),
        Jmp(["ACTION_408_ret_23"]),
        SetSpriteSequence(
            index=0,
            sprite_offset=1,
            is_mold=True,
            is_sequence=True,
            looping=True,
            identifier="ACTION_408_set_sprite_sequence_14"),
        Jmp(["ACTION_408_ret_23"]),
        SetSpriteSequence(
            index=3,
            sprite_offset=1,
            is_mold=True,
            is_sequence=True,
            looping=True,
            identifier="ACTION_408_set_sprite_sequence_16"),
        Jmp(["ACTION_408_ret_23"]),
        SetSpriteSequence(
            index=2,
            sprite_offset=1,
            is_mold=True,
            is_sequence=True,
            looping=True,
            identifier="ACTION_408_set_sprite_sequence_18"),
        Jmp(["ACTION_408_ret_23"]),
        SetSpriteSequence(
            index=4,
            sprite_offset=1,
            is_mold=True,
            is_sequence=True,
            looping=True,
            identifier="ACTION_408_set_sprite_sequence_20"),
        Jmp(["ACTION_408_ret_23"]),
        SetSpriteSequence(
            index=1,
            sprite_offset=1,
            is_mold=True,
            is_sequence=True,
            looping=True,
            identifier="ACTION_408_set_sprite_sequence_22"),
        Return(identifier="ACTION_408_ret_23"),
    ]
)
