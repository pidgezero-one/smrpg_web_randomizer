"""A0749_STAR_HILL_1ST_ROOM_SOUTHEAST_SACKIT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShiftToXYCoords(x=4, y=103),
        ShadowOff(),
        FaceSoutheast(),
        SetSequenceSpeed(VERY_FAST),
        SequenceLoopingOn(),
        VisibilityOn(),
        WalkSoutheastSteps(8),
        Pause(8),
        WalkNortheastSteps(8),
        SetPriority(3),
        WalkSoutheastSteps(4),
        Pause(8),
        WalkSouthwestSteps(16),
        Pause(8),
        ShadowOn(),
        JumpToHeight(128),
        SetWalkingSpeed(FASTER),
        WalkSouthwestSteps(5),
        Pause(64),
        SetWalkingSpeed(VERY_FAST),
        SetSequenceSpeed(FASTEST),
        WalkSouthwestSteps(8),
        VisibilityOff(),
        Return(),
    ]
)
