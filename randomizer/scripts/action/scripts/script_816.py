"""A0816_LANDS_END_VERTICAL_MOVING_PLATFORM"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShadowOn(),
        SetWalkingSpeed(SLOW),
        ShiftZUpSteps(2, identifier="ACTION_816_shift_z_up_steps_2"),
        ShiftZDownSteps(2),
        Jmp(["ACTION_816_shift_z_up_steps_2"]),
    ]
)
