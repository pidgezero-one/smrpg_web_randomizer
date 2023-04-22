"""A0586_SEASIDE_OCCUPIED_CUSTOMER"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FaceNorthwest(),
        FixedFCoordOn(),
        SequenceLoopingOn(),
        SetSequenceSpeed(FAST),
        SetWalkingSpeed(VERY_SLOW),
        WalkNortheastSteps(2, identifier="ACTION_586_shift_northeast_steps_5"),
        WalkSouthwestSteps(3),
        WalkNortheastSteps(1),
        Jmp(["ACTION_586_shift_northeast_steps_5"]),
    ]
)
