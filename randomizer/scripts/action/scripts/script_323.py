"""A0323_MARRYMORE_INNKEEPER_OVERSTAY_TAKE_COINS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ClearBit(TEMP_7042_0),
        ClearBit(TEMP_7042_1),
        ClearBit(TEMP_7042_2),
        ClearBit(TEMP_7042_3),
        ClearBit(TEMP_7042_4),
        ClearBit(TEMP_7042_5),
        ClearBit(TEMP_7042_7),
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(NORMAL),
        WalkNorthwestSteps(2),
        WalkNortheastSteps(3),
        WalkNorthwestSteps(4),
        WalkSouthwestSteps(4),
        WalkSoutheastPixels(12),
        SetSequenceSpeed(SLOW),
        ClearBit(TEMP_7043_1),
        Return(),
    ]
)
