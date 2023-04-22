"""A0865_MOVE_HINOPIO_TO_ARMOR_SHOP"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ClearBit(TEMP_7043_1),
        SetBit(TEMP_7043_3),
        SetAllSpeeds(FASTEST),
        WalkSoutheastSteps(8),
        FaceSouthwest(),
        Return(),
    ]
)
