"""A0850_BOOSTER_PASS_APPRENTICE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(),
        SetWalkingSpeed(FAST),
        WalkSouthwestPixels(4),
        WalkSoutheastSteps(2),
        WalkSoutheastPixels(4),
        StartLoopNTimes(17, identifier="ACTION_850_start_loop_n_times_5"),
        JumpToHeight(108),
        WalkSoutheastSteps(2),
        EndLoop(),
        Pause(48),
        FaceSouthwest(),
        Pause(5),
        FaceNorthwest(),
        Pause(24),
        StartLoopNTimes(17),
        JumpToHeight(108),
        WalkNorthwestSteps(2),
        EndLoop(),
        Pause(48),
        FaceNortheast(),
        Pause(5),
        FaceSoutheast(),
        Pause(24),
        Jmp(["ACTION_850_start_loop_n_times_5"]),
    ]
)
