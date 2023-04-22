"""A0099_LOOPED_JUMPING"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FloatingOn(identifier="ACTION_99_floating_on_0"),
        SetSolidityBits(cant_pass_walls=True),
        JumpToHeight(height=64, silent=True),
        Pause(1, identifier="ACTION_99_pause_3"),
        JmpIfObjectInAir(DUMMY_0X07, ["ACTION_99_pause_3"]),
        FloatingOff(),
        ClearSolidityBits(cant_pass_walls=True),
        JmpIfBitSet(TEMP_7043_1, ["ACTION_99_ret_9"]),
        Jmp(["ACTION_99_floating_on_0"]),
        Return(identifier="ACTION_99_ret_9"),
    ]
)
