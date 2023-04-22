"""A1009_KEEP_DARK_ROOM_GOOMBA_RUNS_FROM_CHEST"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(FAST),
        SetSequenceSpeed(VERY_FAST),
        SequenceLoopingOn(),
        WalkSoutheastSteps(14),
        JumpToHeight(80),
        WalkSoutheastSteps(2),
        SetWalkingSpeed(FASTEST),
        ShadowOff(),
        WalkSouthSteps(10),
        VisibilityOff(),
        Return(),
    ]
)
