"""A0399_JUMPING_FALLING_STATE_IN_FACTORY"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSolidityBits(cant_pass_walls=True),
        JumpToHeight(height=0, silent=True),
        Return(),
    ]
)
