"""A0864_MOVE_HINOPIO_TO_INN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ClearBit(TEMP_7043_1),
        SetBit(TEMP_7043_2),
        SetAllSpeeds(VERY_FAST),
        WalkSoutheastSteps(4),
        FaceSouthwest(),
        Return(),
    ]
)
