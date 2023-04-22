"""A0995_KEEP_BRIDGE_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(SLOW),
        WalkSouthwestSteps(4, identifier="ACTION_995_shift_southwest_steps_2"),
        SetSequenceSpeed(VERY_FAST),
        SetWalkingSpeed(NORMAL),
        WalkSouthwestSteps(3),
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(SLOW),
        WalkSouthwestSteps(4),
        WalkNorthwestSteps(1),
        WalkNortheastSteps(4),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(VERY_SLOW),
        WalkNortheastSteps(2),
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(SLOW),
        WalkNortheastSteps(5),
        WalkSoutheastSteps(1),
        Jmp(["ACTION_995_shift_southwest_steps_2"]),
    ]
)
