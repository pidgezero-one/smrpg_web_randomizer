"""A0365_BOOSTER_HILL_LEFTOVER_FLOWERS_PICKED_UP"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        PlaySound(sound=SO085_FLOWER, channel=4),
        SetVRAMPriority(PRIORITY_3),
        SetPriority(3),
        SetWalkingSpeed(NORMAL),
        FloatingOff(),
        JumpToHeight(112),
        Pause(12),
        FloatingOff(),
        StartLoopNTimes(8),
        VisibilityOn(),
        Pause(4),
        VisibilityOff(),
        Pause(1),
        EndLoop(),
        Return(),
    ]
)
