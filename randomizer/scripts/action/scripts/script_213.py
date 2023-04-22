"""A0213_GREEN_YOSHI"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceSouthwest(),
        SetSequenceSpeed(FAST),
        SequenceLoopingOn(),
        SetVarToConst(ROSE_WAY_703E, 3),
        Return(),
    ]
)
