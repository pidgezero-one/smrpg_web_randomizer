"""A0496_MUSHROOM_DERBY_REFEREE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(SLOW),
        WalkNorthwestSteps(1),
        WalkSouthwestSteps(2),
        WalkSouthwestPixels(8),
        FaceSoutheast(),
        SetSequenceSpeed(SLOW),
        Return(),
    ]
)
