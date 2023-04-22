"""A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        JmpIfBitClear(TEMP_707C_1, ["ACTION_2_start_loop_n_times_3"]),
        ClearSolidityBits(bit_4=True, cant_walk_through=True),
        StartLoopNTimes(15, identifier="ACTION_2_start_loop_n_times_3"),
        Pause(2),
        VisibilityOff(),
        Pause(2),
        VisibilityOn(),
        EndLoop(),
        SetSolidityBits(bit_4=True, cant_walk_through=True),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        Return(),
    ]
)
