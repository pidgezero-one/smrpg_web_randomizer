"""A0212_GREEN_YOSHI"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceNortheast(),
        SetSequenceSpeed(FAST),
        SequenceLoopingOn(),
        SetVarToConst(ROSE_WAY_703E, 7),
        Return(),
    ]
)
