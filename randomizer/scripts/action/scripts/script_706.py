"""A0706_MOLEVILLE_LIBERATED_ENTRANCE_MOLE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(3),
        SetAllSpeeds(SLOW),
        WalkFDirectionSteps(2, identifier="ACTION_706_shift_f_direction_steps_2"),
        Pause(20),
        TurnClockwise45DegreesNTimes(2),
        Pause(20),
        TurnClockwise45DegreesNTimes(6),
        Pause(8),
        TurnClockwise45DegreesNTimes(6),
        Pause(20),
        TurnClockwise45DegreesNTimes(6),
        Jmp(["ACTION_706_shift_f_direction_steps_2"]),
    ]
)
