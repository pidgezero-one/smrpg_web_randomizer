"""A0530_MUSHROOM_WAY_1_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(SLOW),
        SetSequenceSpeed(FASTER),
        WalkNorthwestSteps(10, identifier="ACTION_530_shift_northwest_steps_2"),
        WalkSouthwestSteps(2),
        WalkNorthwestSteps(6),
        WalkSouthwestSteps(1),
        WalkNorthwestSteps(5),
        VisibilityOff(),
        ShiftToXYCoords(x=12, y=11),
        VisibilityOn(),
        WalkSouthwestSteps(4),
        WalkSoutheastSteps(6),
        WalkSouthwestSteps(3),
        WalkSoutheastSteps(8),
        WalkNortheastSteps(1),
        WalkSoutheastSteps(4),
        WalkSouthwestSteps(1),
        WalkSoutheastSteps(1),
        WalkSouthwestSteps(1),
        WalkSoutheastSteps(1),
        WalkSouthwestSteps(5),
        WalkNorthwestSteps(1),
        WalkSouthwestSteps(2),
        Jmp(["ACTION_530_shift_northwest_steps_2"]),
    ]
)
