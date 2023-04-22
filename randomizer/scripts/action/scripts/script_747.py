"""A0747_STAR_HILL_1ST_ROOM_NORTH_SACKIT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShiftToXYCoords(x=2, y=84),
        ShadowOff(),
        FaceSoutheast(),
        SetSequenceSpeed(VERY_FAST),
        SequenceLoopingOn(),
        VisibilityOn(),
        StartLoopNTimes(2),
        WalkSoutheastSteps(4),
        WalkNortheastSteps(4),
        EndLoop(),
        WalkSoutheastSteps(2),
        Pause(8),
        ShadowOn(),
        JumpToHeight(128),
        SetWalkingSpeed(FASTER),
        WalkSoutheastSteps(5),
        Pause(64),
        SetWalkingSpeed(VERY_FAST),
        SetSequenceSpeed(FASTEST),
        WalkSoutheastSteps(10),
        VisibilityOff(),
        Return(),
    ]
)
