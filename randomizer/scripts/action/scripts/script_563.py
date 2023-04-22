"""A0563_WHILE_RECRUITABLE_CHARACTER_CAPTIVE_IN_MUSHROOM_WAY_2"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        StartLoopNTimes(15),
        Pause(2),
        VisibilityOff(),
        Pause(2),
        VisibilityOn(),
        EndLoop(),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        Return(),
    ]
)
