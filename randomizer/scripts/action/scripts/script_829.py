"""A0829_KEEP_XY_PLATFORMS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(index=0, is_sequence=True, looping=True),
        SetPriority(3),
        SetWalkingSpeed(NORMAL),
        Set700CToPressedButton(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 28, ["ACTION_829_shift_f_direction_steps_9"]
        ),
        WalkFDirectionSteps(8, identifier="ACTION_829_shift_f_direction_steps_5"),
        Pause(16),
        TurnClockwise45DegreesNTimes(4),
        Jmp(["ACTION_829_shift_f_direction_steps_5"]),
        WalkFDirectionSteps(2, identifier="ACTION_829_shift_f_direction_steps_9"),
        Pause(4),
        TurnClockwise45DegreesNTimes(6),
        Jmp(["ACTION_829_shift_f_direction_steps_9"]),
    ]
)
