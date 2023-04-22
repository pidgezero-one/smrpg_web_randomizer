"""A0605_MIDAS_1ST_TUNNEL_TROOPA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(3, identifier="ACTION_605_set_priority_0"),
        WalkFDirectionSteps(3),
        SetAllSpeeds(FAST),
        ShiftZUpPixels(8),
        DecZCoord1Step(),
        AddZCoord1Step(),
        ShiftZDownPixels(8),
        SetAllSpeeds(NORMAL),
        TurnClockwise45DegreesNTimes(4),
        WalkFDirectionSteps(3),
        TurnClockwise45DegreesNTimes(4),
        Jmp(["ACTION_605_set_priority_0"]),
    ]
)
