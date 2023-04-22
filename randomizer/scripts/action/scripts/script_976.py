"""A0976_CLOUD_LANDING_BLUE_PUFF_SPAWNER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetVarToConst(TEMP_7034, 1),
        Db(bytearray(b"\xc7\x07")),
        StartLoopNTimes(2),
        AddConstToVar(TEMP_7034, 1),
        AddConstToVar(Z_COORD_1, 8),
        CreatePacketAt7010(
            packet=P032_BLUE_CLOUD, destinations=["ACTION_976_end_loop_7"]
        ),
        Pause(2),
        EndLoop(identifier="ACTION_976_end_loop_7"),
        SetVarToConst(TEMP_7034, 1),
        Db(bytearray(b"\xc7\x07")),
        StartLoopNTimes(2),
        AddConstToVar(TEMP_7034, 1),
        AddConstToVar(Z_COORD_1, 8),
        CreatePacketAt7010(
            packet=P032_BLUE_CLOUD, destinations=["ACTION_976_end_loop_15"]
        ),
        Pause(2),
        EndLoop(identifier="ACTION_976_end_loop_15"),
        Return(),
    ]
)
