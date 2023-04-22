"""A0219_GREEN_YOSHI"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceSouth(),
        SetSequenceSpeed(FAST),
        SequenceLoopingOn(),
        SetVarToConst(ROSE_WAY_703E, 2),
        Return(),
    ]
)
