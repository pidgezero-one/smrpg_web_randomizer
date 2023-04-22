"""A1013_KEEP_DARK_ROOM_KAMIKAZE_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FixedFCoordOn(),
        JumpToHeight(96),
        SetWalkingSpeed(FAST),
        WalkSoutheastSteps(3),
        SetSequenceSpeed(VERY_FAST),
        SequenceLoopingOn(),
        SetWalkingSpeed(FASTEST),
        ShadowOff(),
        WalkSouthSteps(10),
        VisibilityOff(),
        Return(),
    ]
)
