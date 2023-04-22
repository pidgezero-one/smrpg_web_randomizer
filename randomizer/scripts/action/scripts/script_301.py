"""A0301_MARRYMORE_BELLHOP_WHILE_PLAYER_WORKING"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FloatingOn(),
        SetSolidityBits(cant_pass_walls=True),
        SetSequenceSpeed(FAST),
        WalkSoutheastSteps(2),
        WalkNortheastSteps(2),
        VisibilityOff(),
        Return(),
    ]
)
