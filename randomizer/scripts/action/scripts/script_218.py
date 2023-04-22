"""A0218_GREEN_YOSHI"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceNorth(),
        SetSequenceSpeed(FAST),
        SequenceLoopingOn(),
        SetVarToConst(ROSE_WAY_703E, 6),
        Return(),
    ]
)
