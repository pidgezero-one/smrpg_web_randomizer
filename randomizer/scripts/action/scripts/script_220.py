"""A0220_GREEN_YOSHI"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceWest(),
        SetSequenceSpeed(FAST),
        SequenceLoopingOn(),
        SetVarToConst(ROSE_WAY_703E, 4),
        Return(),
    ]
)
