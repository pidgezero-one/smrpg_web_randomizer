"""A0891_MARRYMORE_BELLHOP_AFTER_PAYING_FOR_OVERSTAY"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Pause(144),
        FixedFCoordOn(),
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(SLOW),
        Walk1StepNorthwest(),
        SetSequenceSpeed(SLOW),
        Pause(48),
        SetSequenceSpeed(FAST),
        Walk1StepSoutheast(),
        SetSequenceSpeed(SLOW),
        SequenceLoopingOn(),
        Return(),
    ]
)
