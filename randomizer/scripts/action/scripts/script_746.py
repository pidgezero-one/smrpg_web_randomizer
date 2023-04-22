"""A0746_STAR_HILL_1ST_ROOM_SOUTH_SACKIT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShiftToXYCoords(x=12, y=120),
        ShadowOff(),
        FaceNorthwest(),
        SetSequenceSpeed(VERY_FAST),
        SequenceLoopingOn(),
        VisibilityOn(),
        WalkNorthwestSteps(12),
        WalkNortheastSteps(3),
        WalkToXYCoords(x=8, y=95),
        WalkNorthPixels(4),
        WalkNortheastSteps(12),
        Pause(8),
        ShadowOn(),
        JumpToHeight(128),
        SetWalkingSpeed(FASTER),
        WalkNortheastSteps(5),
        Pause(56),
        SetWalkingSpeed(VERY_FAST),
        SetSequenceSpeed(FASTEST),
        WalkNortheastSteps(8),
        VisibilityOff(),
        Return(),
    ]
)
