"""A0188_ABYSS_BOLT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Pause(1, identifier="ACTION_188_pause_0"),
        FaceSouthwest(),
        FixedFCoordOn(),
        SetWalkingSpeed(NORMAL),
        JmpIfBitClear(TEMP_7043_1, ["ACTION_188_pause_0"]),
        JmpIfBitClear(TEMP_7044_6, ["ACTION_188_pause_0"]),
        Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 4, ["ACTION_188_jmp_if_var_equals_const_18"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 3, ["ACTION_188_jmp_if_var_equals_const_18"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 2, ["ACTION_188_jmp_if_var_equals_const_18"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 1, ["ACTION_188_jmp_if_var_equals_const_18"]
        ),
        JmpIfVarEqualsConst(FACTORY_FALL_3, 30, ["ACTION_188_pause_0"]),
        Inc(FACTORY_FALL_3),
        SetSpriteSequence(index=1, looping=False),
        WalkNortheastPixels(5),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7044_6),
        Jmp(["ACTION_188_pause_0"]),
        JmpIfVarEqualsConst(
            FACTORY_FALL_3,
            0,
            ["ACTION_188_pause_0"],
            identifier="ACTION_188_jmp_if_var_equals_const_18",
        ),
        Dec(FACTORY_FALL_3),
        SetSpriteSequence(index=2, looping=False),
        WalkSouthwestPixels(5),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7044_6),
        Jmp(["ACTION_188_pause_0"]),
    ]
)
