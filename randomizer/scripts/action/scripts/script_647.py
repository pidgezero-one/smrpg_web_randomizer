"""A0647_MIDAS_MID_RIGHT_TUNNEL_CAMERA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Pause(30),
        SetWalkingSpeed(SLOW),
        WalkEastSteps(7),
        SetWalkingSpeed(NORMAL),
        WalkEastSteps(2),
        SetWalkingSpeed(SLOW),
        Walk1StepEast(),
        SetWalkingSpeed(NORMAL),
        Return(),
    ]
)
