"""A0699_TOWER_EARLY_CIRCLING_BOMB"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(identifier="ACTION_699_sequence_looping_on_0"),
        SetWalkingSpeed(SLOW),
        Walk1StepNortheast(),
        WalkNorthwestSteps(3),
        Walk1StepSouthwest(),
        WalkSoutheastSteps(3),
        Jmp(["ACTION_699_sequence_looping_on_0"]),
    ]
)
