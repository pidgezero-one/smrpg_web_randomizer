"""A0529_MUSHROOM_WAY_1_GOOMBA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(SLOW),
        SetSequenceSpeed(FASTER),
        WalkSouthwestSteps(1, identifier="ACTION_529_shift_southwest_steps_2"),
        WalkSoutheastSteps(4),
        WalkSouthwestSteps(6),
        WalkNorthwestSteps(1),
        WalkSouthwestSteps(3),
        WalkNorthwestSteps(8),
        WalkSouthwestSteps(1),
        WalkNorthwestSteps(6),
        WalkSouthwestSteps(2),
        WalkNorthwestSteps(7),
        VisibilityOff(),
        ShiftToXYCoords(x=12, y=11),
        VisibilityOn(),
        ClearSolidityBits(cant_pass_walls=True),
        WalkSouthwestSteps(4),
        WalkSoutheastSteps(2),
        WalkSouthwestSteps(1),
        WalkSoutheastSteps(4),
        WalkSouthwestSteps(1),
        WalkSoutheastSteps(4),
        WalkNortheastSteps(1),
        SetSolidityBits(cant_pass_walls=True),
        WalkSoutheastSteps(6),
        Jmp(["ACTION_529_shift_southwest_steps_2"]),
    ]
)
