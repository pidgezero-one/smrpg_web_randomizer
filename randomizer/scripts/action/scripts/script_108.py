"""A0108_MK_HALL_REPEATING_HENCHMEN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        StartLoopNTimes(2),
        Db(bytearray(b" \x04")),
        Db(bytearray(b"%\xc0\x06\x80\xff")),
        Walk1StepSouthwest(),
        WalkSouthwestPixels(11),
        BPL262728(),
        Pause(2),
        EndLoop(),
        SetSolidityBits(cant_pass_walls=True),
        JumpToHeight(height=108, silent=True),
        Walk1StepSouthwest(),
        WalkSouthwestPixels(14),
        Pause(2),
        Db(bytearray(b" \x04")),
        Db(bytearray(b"%\xc0\x06\x80\xff")),
        Walk1StepSouthwest(),
        WalkSouthwestPixels(11),
        BPL262728(),
        WalkSouthwestPixels(8),
        ClearSolidityBits(cant_pass_walls=True),
        ClearSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        VisibilityOff(),
        Return(),
    ]
)
