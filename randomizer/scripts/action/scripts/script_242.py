"""A0242_SMITHY_COMPONENT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(SLOW, identifier="ACTION_242_set_animation_speed_0"),
        ShiftZDownPixels(2),
        ShiftZUpPixels(2),
        JmpIfBitSet(TEMP_7043_1, ["ACTION_988_ret_14"]),
        Jmp(["ACTION_242_set_animation_speed_0"]),
    ]
)
