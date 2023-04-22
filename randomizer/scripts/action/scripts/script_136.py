"""A0136_MK_OCCUPIED_EXTERIOR_REPEATING_HENCHMEN"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOn(),
        JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
        JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
        SetSolidityBits(cant_pass_walls=True),
        StartLoopNTimes(1),
        Db(bytearray(b" \x04")),
        Db(bytearray(b"%\xc0\x06\x80\xff")),
        Walk1StepSouthwest(),
        WalkSouthwestPixels(14),
        Pause(2),
        BPL262728(),
        EndLoop(),
        ClearSolidityBits(cant_pass_walls=True),
        JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
        JmpToSubroutine(["ACTION_104_set_animation_speed_0"]),
        Pause(20),
        VisibilityOff(),
        ClearSolidityBits(bit_4=True),
        ClearSolidityBits(cant_walk_through=True),
        Return(),
    ]
)
