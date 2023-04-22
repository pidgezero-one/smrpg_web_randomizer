"""A0761_STAR_HILL_2ND_ROOM_WEST_SACKIT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShiftToXYCoords(x=3, y=51),
        ShadowOff(),
        FaceNortheast(),
        SetSequenceSpeed(VERY_FAST),
        SequenceLoopingOn(),
        VisibilityOn(),
        WalkNortheastSteps(8),
        WalkSoutheastSteps(4),
        WalkNortheastSteps(12),
        WalkNorthwestSteps(12),
        WalkNortheastSteps(4),
        FaceNorthwest(),
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
