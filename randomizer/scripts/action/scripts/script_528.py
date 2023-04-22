"""A0528_MUSHROOM_WAY_1_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(SLOW),
        SetSequenceSpeed(FASTER),
        WalkSouthwestSteps(1, identifier="ACTION_528_shift_southwest_steps_2"),
        WalkSoutheastSteps(12),
        WalkSouthwestSteps(3),
        WalkSoutheastSteps(1),
        WalkSouthwestSteps(4),
        WalkNorthwestSteps(1),
        WalkSouthwestSteps(2),
        WalkNorthwestSteps(6),
        WalkSouthwestSteps(1),
        WalkNorthwestSteps(7),
        WalkSouthwestSteps(2),
        WalkNorthwestSteps(8),
        VisibilityOff(),
        ShiftToXYCoords(x=12, y=11),
        VisibilityOn(),
        WalkSouthwestSteps(2),
        WalkSoutheastSteps(1),
        WalkSouthwestSteps(1),
        WalkSoutheastSteps(1),
        WalkSouthwestSteps(1),
        WalkSoutheastSteps(3),
        WalkSouthwestSteps(1),
        WalkSoutheastSteps(2),
        Jmp(["ACTION_528_shift_southwest_steps_2"]),
    ]
)
