"""A0991_SMITHY_COMPONENT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(FAST),
        WalkNortheastPixels(2),
        SetWalkingSpeed(SLOW),
        WalkSouthPixels(4),
        WalkSouthwestPixels(6),
        Pause(12),
        SetWalkingSpeed(FAST),
        WalkNortheastPixels(8),
        SetWalkingSpeed(SLOW),
        WalkSouthwestPixels(4),
        SetWalkingSpeed(VERY_SLOW),
        WalkNorthPixels(4),
        Return(),
    ]
)
