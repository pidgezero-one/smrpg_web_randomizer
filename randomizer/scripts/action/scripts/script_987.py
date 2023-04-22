"""A0987_SMITHY_COMPONENT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpIfBitSet(TEMP_7043_2, ["ACTION_987_set_animation_speed_3"]),
        TransferXYZFPixels(x=250, y=4, z=30, direction=NORTHEAST),
        SetSpriteSequence(index=2, is_sequence=True, looping=True),
        SetWalkingSpeed(NORMAL, identifier="ACTION_987_set_animation_speed_3"),
        ShiftZUpPixels(1),
        Pause(7),
        ShiftZUpPixels(1),
        Pause(11),
        ShiftZDownPixels(1),
        Pause(7),
        ShiftZDownPixels(1),
        Pause(11),
        JmpIfBitSet(TEMP_7043_1, ["ACTION_988_ret_14"]),
        Jmp(["ACTION_987_set_animation_speed_3"]),
    ]
)
