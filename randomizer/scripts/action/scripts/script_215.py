"""A0215_SANCTUARY_CAMERA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetBit(TEMP_7042_0),
        SetWalkingSpeed(SLOW),
        WalkSouthwestSteps(6),
        ClearBit(TEMP_7042_0),
        Return(),
    ]
)
