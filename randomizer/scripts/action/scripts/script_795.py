"""A0795_MUSHROOM_DERBY_UNKNOWN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetVarToRandom(
            PRIMARY_TEMP_700C, 80, identifier="ACTION_795_set_var_to_random_0"
        ),
        Compare700CToVar(Z_COORD_2),
        JmpIfComparisonResultIsGreaterOrEqual(["ACTION_795_jmp_to_subroutine_9"]),
        Compare700CToVar(TEMP_7030),
        JmpIfComparisonResultIsGreaterOrEqual(["ACTION_795_jmp_to_subroutine_13"]),
        JmpToSubroutine(["ACTION_795_set_animation_speed_17"]),
        JmpToSubroutine(["ACTION_795_dec_short_42"]),
        JmpIfVarEqualsConst(TEMP_702E, 1, ["ACTION_795_shift_northeast_pixels_29"]),
        Jmp(["ACTION_795_set_var_to_random_0"]),
        JmpToSubroutine(
            ["ACTION_795_set_animation_speed_25"],
            identifier="ACTION_795_jmp_to_subroutine_9",
        ),
        JmpToSubroutine(["ACTION_795_dec_short_42"]),
        JmpIfVarEqualsConst(TEMP_702E, 1, ["ACTION_795_shift_northeast_pixels_29"]),
        Jmp(["ACTION_795_set_var_to_random_0"]),
        JmpToSubroutine(
            ["ACTION_795_set_animation_speed_21"],
            identifier="ACTION_795_jmp_to_subroutine_13",
        ),
        JmpToSubroutine(["ACTION_795_dec_short_42"]),
        JmpIfVarEqualsConst(TEMP_702E, 1, ["ACTION_795_shift_northeast_pixels_29"]),
        Jmp(["ACTION_795_set_var_to_random_0"]),
        SetSequenceSpeed(FAST, identifier="ACTION_795_set_animation_speed_17"),
        SetWalkingSpeed(VERY_SLOW),
        Walk1StepNortheast(),
        Return(),
        SetSequenceSpeed(FAST, identifier="ACTION_795_set_animation_speed_21"),
        SetWalkingSpeed(SLOW),
        Walk1StepNortheast(),
        Return(),
        SetSequenceSpeed(VERY_FAST, identifier="ACTION_795_set_animation_speed_25"),
        SetWalkingSpeed(NORMAL),
        Walk1StepNortheast(),
        Return(),
        WalkNortheastPixels(8, identifier="ACTION_795_shift_northeast_pixels_29"),
        JmpIfBitClear(
            UNKNOWN_MUSHROOM_DERBY_7085_4, ["ACTION_795_set_animation_speed_39"]
        ),
        JmpIfBitSet(TEMP_7043_5, ["ACTION_795_set_animation_speed_39"]),
        JmpIfBitSet(TEMP_7043_6, ["ACTION_795_set_animation_speed_39"]),
        JmpIfBitSet(TEMP_7044_6, ["ACTION_795_set_animation_speed_39"]),
        SetBit(TEMP_7043_7),
        WalkNortheastPixels(8),
        SetSequenceSpeed(SLOW),
        FaceSouthwest(),
        Jmp(["ACTION_677_jmp_if_random_above_66_0"]),
        SetSequenceSpeed(SLOW, identifier="ACTION_795_set_animation_speed_39"),
        WalkNortheastPixels(8),
        Return(),
        Dec(TEMP_702E, identifier="ACTION_795_dec_short_42"),
        Return(),
    ]
)
