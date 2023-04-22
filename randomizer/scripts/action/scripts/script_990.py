"""A0990_SMITHY_COMPONENT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(FAST),
        WalkNortheastPixels(2),
        WalkSouthwestPixels(2),
        SetWalkingSpeed(SLOW),
        ShiftZDownPixels(2),
        SetWalkingSpeed(VERY_SLOW),
        ShiftZDownPixels(2),
        Pause(17),
        SetWalkingSpeed(FAST),
        ShiftZUpPixels(4),
        WalkNortheastPixels(2),
        SetWalkingSpeed(NORMAL),
        WalkSouthwestPixels(4),
        SetWalkingSpeed(SLOW),
        WalkNortheastPixels(2),
        Return(),
    ]
)
