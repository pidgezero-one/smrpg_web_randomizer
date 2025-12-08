"""A0190_ABYSS_BOLT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Pause(1, identifier="ACTION_190_pause_0"),
        FaceSoutheast(),
        FixedFCoordOn(),
        SetWalkingSpeed(NORMAL),
        JmpIfBitClear(TEMP_7043_3, ["ACTION_190_pause_0"]),
        JmpIfBitClear(TEMP_7044_6, ["ACTION_190_pause_0"]),
        Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 7, ["ACTION_190_jmp_if_var_equals_const_18"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 0, ["ACTION_190_jmp_if_var_equals_const_18"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 1, ["ACTION_190_jmp_if_var_equals_const_18"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 2, ["ACTION_190_jmp_if_var_equals_const_18"]
        ),
        JmpIfVarEqualsConst(FACTORY_FALL_5, 0, ["ACTION_190_pause_0"]),
        Dec(FACTORY_FALL_5),
        SetSpriteSequence(index=1, looping=False, mirror_sprite=True),
        WalkNorthwestPixels(5),
        ClearBit(TEMP_7043_3),
        ClearBit(TEMP_7044_6),
        Jmp(["ACTION_190_pause_0"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_5,
            16,
            ["ACTION_190_pause_0"],
            identifier="ACTION_190_jmp_if_var_equals_const_18"),
        Inc(FACTORY_FALL_5),
        SetSpriteSequence(index=2, looping=False, mirror_sprite=True),
        WalkSoutheastPixels(5),
        ClearBit(TEMP_7043_3),
        ClearBit(TEMP_7044_6),
        Jmp(["ACTION_190_pause_0"]),
    ]
)
