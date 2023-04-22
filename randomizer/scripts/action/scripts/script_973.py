"""A0973_ENDING_CREDITS_CASTLE_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(SLOW),
        SequenceLoopingOn(),
        Walk1StepNortheast(),
        WalkNorthwestSteps(2),
        WalkSouthwestSteps(2),
        WalkSoutheastSteps(3),
        WalkSoutheastPixels(8),
        WalkNortheastSteps(5),
        Walk1StepNorthwest(),
        SetWalkingSpeed(VERY_FAST),
        WalkSouthwestSteps(3),
        FaceNorthwest(),
        JumpToHeight(64),
        Pause(32),
        SequenceLoopingOff(),
        Return(),
    ]
)
