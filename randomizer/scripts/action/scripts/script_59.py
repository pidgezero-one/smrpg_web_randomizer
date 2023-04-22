"""A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 463, ["ACTION_59_set_700C_to_object_coord_23"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 464, ["ACTION_59_set_700C_to_object_coord_23"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 465, ["ACTION_59_set_700C_to_object_coord_23"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 466, ["ACTION_59_set_700C_to_object_coord_23"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 467, ["ACTION_59_set_700C_to_object_coord_23"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 468, ["ACTION_59_set_700C_to_object_coord_23"]
        ),
        ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
        SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
        FaceSouthwest(),
        SetWalkingSpeed(FAST, identifier="ACTION_59_set_animation_speed_10"),
        WalkFDirectionSteps(2),
        Pause(32),
        WalkFDirectionSteps(2),
        Pause(32),
        WalkFDirectionSteps(2),
        Pause(32),
        WalkFDirectionSteps(2),
        Pause(32),
        JumpToHeight(height=60, silent=True),
        WalkFDirectionSteps(2),
        TurnRandomDirection(),
        Jmp(["ACTION_59_set_animation_speed_10"]),
        Set700CToObjectCoord(
            target_npc=DUMMY_0X07,
            coord=COORD_F,
            pixel=True,
            identifier="ACTION_59_set_700C_to_object_coord_23",
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_59_set_sprite_sequence_32"]),
        SetSpriteSequence(index=21, is_mold=True, is_sequence=True, looping=True),
        Pause(8),
        SetSpriteSequence(index=22, is_mold=True, is_sequence=True, looping=True),
        Pause(8),
        JmpIfBitClear(TEMP_7044_7, ["ACTION_59_set_700C_to_object_coord_23"]),
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        Return(),
        SetSpriteSequence(
            index=21,
            is_mold=True,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_59_set_sprite_sequence_32",
        ),
        Pause(8),
        SetSpriteSequence(
            index=22, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True
        ),
        Pause(8),
        JmpIfBitClear(TEMP_7044_7, ["ACTION_59_set_700C_to_object_coord_23"]),
        SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
        Return(),
    ]
)
