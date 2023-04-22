"""A0391_CAMERA_SHAKE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        StartLoopNTimes(7),
        SetWalkingSpeed(FASTEST),
        WalkNorthPixels(4),
        WalkSouthPixels(8),
        WalkNorthPixels(4),
        EndLoop(),
        Return(),
    ]
)
