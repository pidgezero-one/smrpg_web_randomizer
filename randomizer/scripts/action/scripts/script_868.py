"""A0868_MOVE_HINOPIO_TO_ITEM_SHOP"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ClearBit(TEMP_7043_3),
        SetBit(TEMP_7043_1),
        SetAllSpeeds(FASTEST),
        WalkNorthwestSteps(8),
        FaceSouthwest(),
        Return(),
    ]
)
