"""A0022_SLOW_REPEATED_JUMPING"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JumpToHeight(
            height=80, silent=True, identifier="ACTION_22_jump_to_height_silent_0"
        ),
        Pause(1, identifier="ACTION_22_pause_1"),
        JmpIfObjectInAir(DUMMY_0X07, ["ACTION_22_pause_1"]),
        Jmp(["ACTION_22_jump_to_height_silent_0"]),
    ]
)
