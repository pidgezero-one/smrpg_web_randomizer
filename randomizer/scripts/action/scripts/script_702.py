"""A0702_TOWER_FIRST_STAIRCASE_BOSS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        WalkSouthwestSteps(2),
        WalkSouthwestPixels(8),
        WalkSoutheastSteps(3),
        VisibilityOff(),
        Return(),
    ]
)
