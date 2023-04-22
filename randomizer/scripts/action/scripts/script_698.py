"""A0698_TOWER_EARLY_CIRCLING_BOMB"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(identifier="ACTION_698_sequence_looping_on_0"),
        SetWalkingSpeed(SLOW),
        Walk1StepSouthwest(),
        WalkSoutheastSteps(3),
        Walk1StepNortheast(),
        WalkNorthwestSteps(3),
        Jmp(["ACTION_698_sequence_looping_on_0"]),
    ]
)
