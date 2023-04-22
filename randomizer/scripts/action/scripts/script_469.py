"""A0469_BANDITS_WAY_5_LOADER_BOSS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSolidityBits(cant_walk_through=True),
        SequenceLoopingOn(),
        SetSequenceSpeed(NORMAL),
        StartLoopNTimes(119, identifier="ACTION_469_start_loop_n_times_3"),
        Pause(1),
        JmpIfObjectWithinRangeSameZ(
            comparing_npc=MARIO, usually=0, tiles=3, destinations=["ACTION_469_db_7"]
        ),
        Jmp(["ACTION_469_end_loop_8"]),
        UnknownJmp3C(
            0x00, 0x20, ["ACTION_469_set_bit_11"], identifier="ACTION_469_db_7"
        ),
        EndLoop(identifier="ACTION_469_end_loop_8"),
        TurnClockwise45DegreesNTimes(4),
        Jmp(["ACTION_469_start_loop_n_times_3"]),
        SetBit(TEMP_7044_4, identifier="ACTION_469_set_bit_11"),
        Return(),
    ]
)
