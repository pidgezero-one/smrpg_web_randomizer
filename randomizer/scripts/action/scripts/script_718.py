"""A0718_BOOSTER_HILL_BOSS_MOVE_FORWARD"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetBit(TEMP_7044_1),
        WalkNorthwestPixels(32),
        Pause(60),
        StartLoopNTimes(3),
        Pause(30),
        WalkSoutheastPixels(8),
        EndLoop(),
        ClearBit(TEMP_7044_1),
        Return(),
    ]
)
