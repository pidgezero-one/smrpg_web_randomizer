"""A0741_TOWER_MID_CIRCLING_BOMB"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(identifier="ACTION_741_sequence_looping_on_0"),
        SetWalkingSpeed(SLOW),
        Walk1StepNorthwest(),
        Walk1StepSouthwest(),
        Walk1StepSoutheast(),
        Walk1StepNortheast(),
        Jmp(["ACTION_741_sequence_looping_on_0"]),
    ]
)
