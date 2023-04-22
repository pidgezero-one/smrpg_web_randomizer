"""A0430_YOSHI_FINISH_RACE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(),
        ResetProperties(),
        SetSequenceSpeed(VERY_FAST),
        SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3]),
        StartLoopNTimes(15),
        Pause(1),
        EndLoop(),
    ]
)
