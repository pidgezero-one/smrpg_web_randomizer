"""A0417_GOOMBA_THUMPIN_TOP_PIPE"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(SLOW),
        VisibilityOff(),
        TransferToXYZF(x=5, y=115, z=1, direction=EAST),
        JmpIfBitClear(TEMP_7049_6, ["ACTION_417_set_700C_to_pressed_button_5"]),
        SetWalkingSpeed(NORMAL),
        Set700CToPressedButton(identifier="ACTION_417_set_700C_to_pressed_button_5"),
        CompareVarToConst(PRIMARY_TEMP_700C, 25),
        JmpIfComparisonResultIsLesser(["ACTION_417_shift_z_up_pixels_16"]),
        CompareVarToConst(PRIMARY_TEMP_700C, 29),
        JmpIfComparisonResultIsGreaterOrEqual(["ACTION_417_jmp_if_bit_set_28"]),
        JmpIfBitSet(TEMP_7049_6, ["ACTION_417_set_animation_speed_14"]),
        SetWalkingSpeed(NORMAL),
        Pause(6),
        Jmp(["ACTION_417_shift_z_up_pixels_16"]),
        SetWalkingSpeed(FAST, identifier="ACTION_417_set_animation_speed_14"),
        Pause(3),
        ShiftZUpPixels(6, identifier="ACTION_417_shift_z_up_pixels_16"),
        ResetProperties(),
        VisibilityOn(),
        ShiftZUpPixels(10),
        SetSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        Pause(40),
        ClearSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        Pause(4),
        ShiftZDownPixels(10),
        VisibilityOff(),
        BounceToXYWithHeight(x=5, y=115, height=1),
        Jmp(["ACTION_417_transfer_to_xyzf_47"]),
        JmpIfBitSet(
            TEMP_7049_6,
            ["ACTION_417_pause_30"],
            identifier="ACTION_417_jmp_if_bit_set_28"),
        Pause(1),
        Pause(1, identifier="ACTION_417_pause_30"),
        TransferXYZFPixels(x=254, y=0, z=0, direction=EAST),
        ShiftZUpPixels(4),
        ResetProperties(),
        VisibilityOn(),
        ShiftZUpPixels(10),
        SetSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        Pause(28),
        ClearSolidityBits(
            bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
        ),
        Pause(2),
        ShiftZDownPixels(10),
        VisibilityOff(),
        BounceToXYWithHeight(x=5, y=115, height=1),
        JmpIfBitSet(TEMP_7049_6, ["ACTION_417_pause_45"]),
        Pause(1),
        Pause(1, identifier="ACTION_417_pause_45"),
        Jmp(["ACTION_417_transfer_to_xyzf_47"]),
        TransferToXYZF(
            x=8, y=60, z=0, direction=EAST, identifier="ACTION_417_transfer_to_xyzf_47"
        ),
        ClearBit(TEMP_7044_1),
        Return(),
    ]
)
