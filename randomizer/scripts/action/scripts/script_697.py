"""A0697_TOWER_EARLY_CIRCLING_BOMB"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(identifier="ACTION_697_sequence_looping_on_0"),
        SetWalkingSpeed(NORMAL),
        WalkSoutheastSteps(3),
        Walk1StepNortheast(),
        WalkNorthwestSteps(3),
        Walk1StepSouthwest(),
        Jmp(["ACTION_697_sequence_looping_on_0"]),
    ]
)
