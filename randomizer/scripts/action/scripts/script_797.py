"""A0797_MUSHROOM_DERBY_UNKNOWN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetVarToRandom(
            PRIMARY_TEMP_700C, 80, identifier="ACTION_797_set_var_to_random_0"
        ),
        Compare700CToVar(ROSE_WAY_7038),
        JmpIfComparisonResultIsGreaterOrEqual(["ACTION_797_jmp_to_subroutine_9"]),
        Compare700CToVar(ROSE_WAY_703A),
        JmpIfComparisonResultIsGreaterOrEqual(["ACTION_797_jmp_to_subroutine_13"]),
        JmpToSubroutine(["ACTION_797_set_animation_speed_17"]),
        JmpToSubroutine(["ACTION_797_dec_short_43"]),
        JmpIfVarEqualsConst(Z_COORD_1, 1, ["ACTION_797_shift_northeast_pixels_29"]),
        Jmp(["ACTION_797_set_var_to_random_0"]),
        JmpToSubroutine(
            ["ACTION_797_set_animation_speed_25"],
            identifier="ACTION_797_jmp_to_subroutine_9",
        ),
        JmpToSubroutine(["ACTION_797_dec_short_43"]),
        JmpIfVarEqualsConst(Z_COORD_1, 1, ["ACTION_797_shift_northeast_pixels_29"]),
        Jmp(["ACTION_797_set_var_to_random_0"]),
        JmpToSubroutine(
            ["ACTION_797_set_animation_speed_21"],
            identifier="ACTION_797_jmp_to_subroutine_13",
        ),
        JmpToSubroutine(["ACTION_797_dec_short_43"]),
        JmpIfVarEqualsConst(Z_COORD_1, 1, ["ACTION_797_shift_northeast_pixels_29"]),
        Jmp(["ACTION_797_set_var_to_random_0"]),
        SetSequenceSpeed(FAST, identifier="ACTION_797_set_animation_speed_17"),
        SetWalkingSpeed(VERY_SLOW),
        Walk1StepNortheast(),
        Return(),
        SetSequenceSpeed(FAST, identifier="ACTION_797_set_animation_speed_21"),
        SetWalkingSpeed(SLOW),
        Walk1StepNortheast(),
        Return(),
        SetSequenceSpeed(VERY_FAST, identifier="ACTION_797_set_animation_speed_25"),
        SetWalkingSpeed(NORMAL),
        Walk1StepNortheast(),
        Return(),
        WalkNortheastPixels(8, identifier="ACTION_797_shift_northeast_pixels_29"),
        JmpIfBitSet(TEMP_7043_5, ["ACTION_797_set_animation_speed_39"]),
        JmpIfBitSet(TEMP_7043_7, ["ACTION_797_set_animation_speed_39"]),
        JmpIfBitSet(TEMP_7043_6, ["ACTION_797_set_animation_speed_39"]),
        SetBit(TEMP_7044_6),
        ClearBit(UNKNOWN_MUSHROOM_DERBY_7085_4),
        WalkNortheastPixels(8),
        SetSequenceSpeed(SLOW),
        SetVarToConst(Z_COORD_1, 0),
        Return(),
        SetSequenceSpeed(SLOW, identifier="ACTION_797_set_animation_speed_39"),
        WalkNortheastPixels(8),
        SetVarToConst(Z_COORD_1, 0),
        Return(),
        Dec(Z_COORD_1, identifier="ACTION_797_dec_short_43"),
        Return(),
    ]
)
