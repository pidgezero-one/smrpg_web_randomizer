"""A0974_ENDING_CREDITS_CASTLE_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(SLOW),
        WalkSoutheastSteps(2),
        WalkNortheastSteps(2),
        Walk1StepSoutheast(),
        SetWalkingSpeed(FAST),
        WalkSoutheastSteps(2),
        WalkSouthwestSteps(3),
        SetWalkingSpeed(SLOW),
        WalkNorthwestSteps(5),
        WalkNorthwestPixels(8),
        Walk1StepSouthwest(),
        WalkSoutheastPixels(8),
        Pause(24),
        SequenceLoopingOn(),
        JumpToHeight(64),
        Pause(32),
        FaceNorthwest(),
        Pause(32),
        SequenceLoopingOff(),
        Return(),
    ]
)
