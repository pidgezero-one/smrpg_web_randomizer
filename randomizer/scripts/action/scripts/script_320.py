"""A0320_BELLHOP_SET_POSITION"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetBit(TEMP_7042_3),
        SetWalkingSpeed(NORMAL),
        SetSequenceSpeed(FAST),
        Walk1StepNortheast(),
        FaceSouthwest(),
        SetSequenceSpeed(SLOW),
        Return(),
    ]
)
