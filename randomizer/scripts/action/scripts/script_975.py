"""A0975_ENDING_CREDITS_CASTLE_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(SLOW),
        SequenceLoopingOn(),
        WalkSoutheastSteps(9),
        WalkSouthwestSteps(2),
        WalkNorthwestSteps(4),
        SetWalkingSpeed(VERY_FAST),
        WalkNortheastSteps(2),
        FaceNorthwest(),
        JumpToHeight(64),
        Pause(32),
        SequenceLoopingOff(),
        Return(),
    ]
)
