"""A0742_TOWER_MID_CIRCLING_BOMB"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SequenceLoopingOn(identifier="ACTION_742_sequence_looping_on_0"),
        SetWalkingSpeed(SLOW),
        Walk1StepSoutheast(),
        WalkNortheastSteps(3),
        Walk1StepNorthwest(),
        WalkSouthwestSteps(3),
        Jmp(["ACTION_742_sequence_looping_on_0"]),
    ]
)
