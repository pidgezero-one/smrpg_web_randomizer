"""A0208_RAZ_ENDING"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceNortheast(),
        FixedFCoordOn(),
        SetWalkingSpeed(VERY_FAST),
        StartLoopNTimes(1, identifier="ACTION_208_start_loop_n_times_3"),
        WalkNortheastPixels(2),
        WalkSouthwestPixels(2),
        Pause(30),
        EndLoop(),
        Pause(90),
        Jmp(["ACTION_208_start_loop_n_times_3"]),
    ]
)
