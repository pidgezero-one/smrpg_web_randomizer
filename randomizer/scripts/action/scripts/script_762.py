"""A0762_STAR_HILL_2ND_ROOM_CENTRAL_SACKIT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShiftToXYCoords(x=17, y=55),
        ShadowOff(),
        FaceNortheast(),
        SetSequenceSpeed(VERY_FAST),
        SequenceLoopingOn(),
        VisibilityOn(),
        WalkNortheastSteps(3),
        WalkToXYCoords(x=19, y=43),
        WalkNorthwestSteps(20),
        WalkSouthwestSteps(8),
        WalkNorthwestSteps(4),
        Pause(8),
        ShadowOn(),
        JumpToHeight(128),
        SetWalkingSpeed(FASTER),
        WalkNorthwestSteps(5),
        Pause(56),
        SetWalkingSpeed(VERY_FAST),
        SetSequenceSpeed(FASTEST),
        WalkNorthwestSteps(8),
        VisibilityOff(),
        Return(),
    ]
)
