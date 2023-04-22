"""A0531_MUSHROOM_WAY_1_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(SLOW),
        SetSequenceSpeed(FASTER),
        WalkSouthwestSteps(2, identifier="ACTION_531_shift_southwest_steps_2"),
        WalkNorthwestSteps(4),
        WalkSouthwestSteps(1),
        WalkNorthwestSteps(3),
        WalkNortheastSteps(1),
        WalkNorthwestSteps(1),
        VisibilityOff(),
        ShiftToXYCoords(x=12, y=11),
        VisibilityOn(),
        WalkSouthwestSteps(3),
        WalkSoutheastSteps(3),
        WalkSouthwestSteps(4),
        WalkSoutheastSteps(10),
        WalkNortheastSteps(1),
        WalkSoutheastSteps(6),
        WalkSouthwestSteps(9),
        WalkNorthwestSteps(6),
        WalkSouthwestSteps(1),
        WalkNorthwestSteps(7),
        Jmp(["ACTION_531_shift_southwest_steps_2"]),
    ]
)
