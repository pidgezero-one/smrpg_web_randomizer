"""A0101_MK_THRONE_HENCHMAN_BOUNCE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpIfBitSet(TEMP_7043_6, ["ACTION_101_jmp_if_random_above_128_6"]),
        JmpIfRandom1of2(["ACTION_101_transfer_xyzf_pixels_4"]),
        TransferXYZFPixels(x=0, y=0, z=21, direction=EAST),
        Jmp(["ACTION_103_set_animation_speed_15"]),
        TransferXYZFPixels(
            x=0,
            y=0,
            z=14,
            direction=EAST,
            identifier="ACTION_101_transfer_xyzf_pixels_4",
        ),
        Jmp(["ACTION_103_set_animation_speed_23"]),
        JmpIfRandom1of2(
            ["ACTION_101_pause_9"], identifier="ACTION_101_jmp_if_random_above_128_6"
        ),
        Pause(8),
        Jmp(["ACTION_103_clear_solidity_bits_0"]),
        Pause(20, identifier="ACTION_101_pause_9"),
        Jmp(["ACTION_103_clear_solidity_bits_0"]),
    ]
)
