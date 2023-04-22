"""A0736_TOWER_EARLY_CIRCLING_BOMB"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(identifier="ACTION_736_sequence_looping_on_0"),
        SetWalkingSpeed(SLOW),
        WalkNorthwestSteps(2),
        Walk1StepSouthwest(),
        WalkSoutheastSteps(2),
        Walk1StepNortheast(),
        Jmp(["ACTION_736_sequence_looping_on_0"]),
    ]
)
