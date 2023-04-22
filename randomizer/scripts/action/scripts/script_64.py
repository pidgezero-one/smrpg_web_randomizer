"""A0064_KINGDOM_FAST_KID"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(VERY_FAST),
        SetWalkingSpeed(VERY_FAST),
        WalkNortheastSteps(1, identifier="ACTION_64_shift_northeast_steps_2"),
        WalkSoutheastSteps(3),
        WalkSouthwestSteps(4),
        WalkNorthwestSteps(3),
        WalkNortheastSteps(3),
        Jmp(["ACTION_64_shift_northeast_steps_2"]),
    ]
)
