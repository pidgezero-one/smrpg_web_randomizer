"""A0748_STAR_HILL_1ST_ROOM_NORTHWEST_SACKIT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShiftToXYCoords(x=16, y=72),
        ShadowOff(),
        FaceSouthwest(),
        SetSequenceSpeed(FASTER),
        SequenceLoopingOn(),
        VisibilityOn(),
        SetPriority(3),
        WalkSouthwestSteps(11),
        WalkNorthwestSteps(5),
        SetPriority(2),
        Pause(8),
        ShadowOn(),
        JumpToHeight(128),
        SetWalkingSpeed(FASTER),
        WalkNorthwestSteps(5),
        Pause(64),
        SetWalkingSpeed(VERY_FAST),
        SetSequenceSpeed(FASTEST),
        WalkNorthwestSteps(10),
        VisibilityOff(),
        Return(),
    ]
)
