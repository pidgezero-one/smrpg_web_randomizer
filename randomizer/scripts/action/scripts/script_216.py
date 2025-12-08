"""A0216_VINES_1ST_ROOM_VERTICAL_FLYING_BIRD"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpIfRandom1of2(["ACTION_216_set_animation_speed_3"]),
        SetWalkingSpeed(NORMAL),
        Jmp(["ACTION_216_set_6"]),
        SetWalkingSpeed(SLOW, identifier="ACTION_216_set_animation_speed_3"),
        Jmp(["ACTION_216_set_6"]),
        SetWalkingSpeed(FAST),
        SetVarToConst(PRIMARY_TEMP_700C, 3, identifier="ACTION_216_set_6"),
        ShiftZ20Steps(),
        JmpIfRandom1of2(["ACTION_216_jmp_if_bit_set_21"]),
        JmpIfBitSet(TEMP_7043_0, ["ACTION_216_turn_clockwise_45_degrees_n_times_12"]),
        TurnClockwise45DegreesNTimes(2),
        Jmp(["ACTION_216_pause_13"]),
        TurnClockwise45DegreesNTimes(
            6, identifier="ACTION_216_turn_clockwise_45_degrees_n_times_12"
        ),
        Pause(10, identifier="ACTION_216_pause_13"),
        JmpIfRandom1of2(["ACTION_216_set_animation_speed_17"]),
        SetWalkingSpeed(NORMAL),
        Jmp(["ACTION_216_set_6"]),
        SetWalkingSpeed(SLOW, identifier="ACTION_216_set_animation_speed_17"),
        Jmp(["ACTION_216_set_6"]),
        SetWalkingSpeed(FAST),
        Jmp(["ACTION_216_set_6"]),
        JmpIfBitSet(
            TEMP_7043_0,
            ["ACTION_216_turn_clockwise_45_degrees_n_times_28"],
            identifier="ACTION_216_jmp_if_bit_set_21"),
        TurnClockwise45DegreesNTimes(2),
        Pause(4),
        TurnClockwise45DegreesNTimes(2),
        Pause(4),
        SetBit(TEMP_7043_0),
        Jmp(["ACTION_216_set_6"]),
        TurnClockwise45DegreesNTimes(
            6, identifier="ACTION_216_turn_clockwise_45_degrees_n_times_28"
        ),
        Pause(4),
        TurnClockwise45DegreesNTimes(6),
        Pause(4),
        ClearBit(TEMP_7043_0),
        Jmp(["ACTION_216_set_6"]),
    ]
)
