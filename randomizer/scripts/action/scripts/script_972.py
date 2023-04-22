"""A0972_ENDING_CREDITS_CASTLE_ASSISTANT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(),
        WalkNortheastSteps(2),
        Pause(24),
        FaceSoutheast(),
        Pause(24),
        FaceNorthwest(),
        Pause(24),
        FaceSouthwest(),
        Pause(24),
        FaceNortheast(),
        Pause(24),
        SetWalkingSpeed(FAST),
        SetSequenceSpeed(VERY_FAST),
        WalkSouthwestSteps(2),
        Pause(8),
        SetWalkingSpeed(NORMAL),
        SetSequenceSpeed(FAST),
        Pause(16),
        WalkNortheastSteps(3),
        Pause(104),
        WalkSouthwestSteps(8),
        SetWalkingSpeed(FASTER),
        WalkNortheastSteps(7),
        FaceNorthwest(),
        SequenceLoopingOff(),
        Return(),
    ]
)
