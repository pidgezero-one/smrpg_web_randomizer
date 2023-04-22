"""A0636_54_VELOCITY_SINGLE_JUMP"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FloatingOn(),
        SetSolidityBits(cant_pass_walls=True),
        JumpToHeight(height=64, silent=True),
        Pause(1, identifier="ACTION_636_pause_3"),
        JmpIfObjectInAir(DUMMY_0X07, ["ACTION_636_pause_3"]),
        ClearSolidityBits(cant_pass_walls=True),
        FloatingOff(),
        Return(),
    ]
)
