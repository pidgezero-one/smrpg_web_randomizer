"""A0280_KEEP_BUTTON_GAME_BUTTON"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(VERY_FAST),
        WalkSoutheastPixels(8),
        SetWalkingSpeed(NORMAL),
        SetPriority(2),
        SetVarToConst(ROSE_WAY_703C, 0),
    ]
)
