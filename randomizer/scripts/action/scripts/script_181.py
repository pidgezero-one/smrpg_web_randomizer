"""A0181_FAST_AMANITA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOn(),
        SetSequenceSpeed(FASTER),
        SequenceLoopingOn(),
        WalkNortheastSteps(5),
        Pause(24),
        WalkSouthwestSteps(5),
        Pause(72),
        ClearBit(TEMP_7044_0),
        Return(),
    ]
)
