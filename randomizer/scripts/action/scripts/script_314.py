"""A0314_SHIP_TRAMPOLINE_PUZZLE_TRAMPOLINE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(FAST),
        FixedFCoordOn(),
        WalkNortheastSteps(3, identifier="ACTION_314_shift_northeast_steps_2"),
        WalkSouthwestSteps(3),
        Jmp(["ACTION_314_shift_northeast_steps_2"]),
    ]
)
