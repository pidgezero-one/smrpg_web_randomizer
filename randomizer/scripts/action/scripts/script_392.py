"""A0392_SLEEPING_WIGGLER_CAMERA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(FAST, identifier="ACTION_392_set_animation_speed_0"),
        WalkNorthPixels(5),
        WalkSouthPixels(10),
        WalkNorthPixels(5),
        JmpIfBitSet(TEMP_7043_0, ["ACTION_392_ret_6"]),
        Jmp(["ACTION_392_set_animation_speed_0"]),
        Return(identifier="ACTION_392_ret_6"),
    ]
)
