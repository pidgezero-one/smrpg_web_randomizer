"""A0284_IFRAME_BLINK"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Db(bytearray(b"6")),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        JmpIfBitClear(TEMP_707C_1, ["ACTION_284_start_loop_n_times_4"]),
        ClearSolidityBits(bit_4=True, cant_walk_through=True),
        StartLoopNTimes(15, identifier="ACTION_284_start_loop_n_times_4"),
        Pause(2),
        VisibilityOff(),
        Pause(2),
        VisibilityOn(),
        EndLoop(),
        SetSolidityBits(bit_4=True, cant_walk_through=True),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        Db(bytearray(b"7")),
        Return(),
    ]
)
