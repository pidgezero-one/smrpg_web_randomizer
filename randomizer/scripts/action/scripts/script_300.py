"""A0300_MARRYMORE_TOP_FLOOR_BELLHOP_MOVE_IF_WORKING"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(FAST),
        WalkNorthwestSteps(3),
        WalkNortheastSteps(2),
        VisibilityOff(),
        Return(),
    ]
)
