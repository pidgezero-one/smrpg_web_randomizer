"""A0993_KEEP_BRIDGE_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(SLOW),
        WalkNortheastSteps(5, identifier="ACTION_993_shift_northeast_steps_2"),
        FaceSouthwest(),
        FixedFCoordOn(),
        SetSequenceSpeed(NORMAL),
        SetWalkingSpeed(VERY_SLOW),
        WalkNortheastSteps(2),
        FixedFCoordOff(),
        FaceNortheast(),
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(SLOW),
        WalkNortheastSteps(3),
        SetSequenceSpeed(VERY_FAST),
        SetWalkingSpeed(NORMAL),
        WalkNortheastSteps(1),
        WalkSoutheastSteps(1),
        WalkSouthwestSteps(1),
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(SLOW),
        WalkSouthwestSteps(10),
        WalkNorthwestSteps(1),
        Jmp(["ACTION_993_shift_northeast_steps_2"]),
    ]
)
