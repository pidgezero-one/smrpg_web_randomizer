# pylint: disable=C0301

"""E3143_ROSE_WAY_MAIN_ROOM_PLATFORMS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FreezeCamera(),
        CopyVarToVar(
            from_var=TEMP_70AA,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3143_set_7000_to_70A0_short_mem_1"),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7034),
        EnableControlsUntilReturn([X, B]),
        StartSyncEmbeddedActionScript(
            target=SCREEN_FOCUS,
            prefix=0xF1,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASDb(bytearray(b"\xc8\x92")),
                ASAddConstToVar(X_COORD_2, 65532),
                ASAddConstToVar(Y_COORD_2, 65522),
                ASRunAwayShift(),
            ]),
        ActionQueueSync(target=MARIO, subscript=[ASSetWalkingSpeed(FAST)]),
        ActionQueueSync(target=MEM_70AA, subscript=[ASSetWalkingSpeed(FAST)]),
        JmpIfMarioInAir(["EVENT_3143_set_7000_to_pressed_button_11"]),
        Set7000ToTappedButton(),
        JmpIf7000AllBitsClear(
            bits=[], destinations=["EVENT_3143_set_7000_to_pressed_button_11"]
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASDb(bytearray(b"\xfd\x9c\x04")),
                ASJumpToHeight(height=108, silent=True),
            ]),
        Set7000ToPressedButton(identifier="EVENT_3143_set_7000_to_pressed_button_11"),
        Mem7000AndConst(0x000F),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3143_set_short_23"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_3143_set_short_25"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_3143_set_short_27"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_3143_set_short_29"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_3143_set_short_31"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["EVENT_3143_set_short_33"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_3143_set_short_35"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_3143_set_short_37"]),
        CopyVarToVar(from_var=TEMP_7032, to_var=PRIMARY_TEMP_700C),
        Jmp(["EVENT_3143_copy_var_to_var_38"]),
        SetVarToConst(PRIMARY_TEMP_700C, 0, identifier="EVENT_3143_set_short_23"),
        Jmp(["EVENT_3143_copy_var_to_var_38"]),
        SetVarToConst(PRIMARY_TEMP_700C, 1, identifier="EVENT_3143_set_short_25"),
        Jmp(["EVENT_3143_copy_var_to_var_38"]),
        SetVarToConst(PRIMARY_TEMP_700C, 2, identifier="EVENT_3143_set_short_27"),
        Jmp(["EVENT_3143_copy_var_to_var_38"]),
        SetVarToConst(PRIMARY_TEMP_700C, 3, identifier="EVENT_3143_set_short_29"),
        Jmp(["EVENT_3143_copy_var_to_var_38"]),
        SetVarToConst(PRIMARY_TEMP_700C, 4, identifier="EVENT_3143_set_short_31"),
        Jmp(["EVENT_3143_copy_var_to_var_38"]),
        SetVarToConst(PRIMARY_TEMP_700C, 5, identifier="EVENT_3143_set_short_33"),
        Jmp(["EVENT_3143_copy_var_to_var_38"]),
        SetVarToConst(PRIMARY_TEMP_700C, 6, identifier="EVENT_3143_set_short_35"),
        Jmp(["EVENT_3143_copy_var_to_var_38"]),
        SetVarToConst(PRIMARY_TEMP_700C, 7, identifier="EVENT_3143_set_short_37"),
        CopyVarToVar(
            from_var=PRIMARY_TEMP_700C,
            to_var=TEMP_7032,
            identifier="EVENT_3143_copy_var_to_var_38"),
        ClearBit(TEMP_7043_4),
        Set7016701BToObjectXYZ(MEM_70AA),
        StartSyncEmbeddedActionScript(
            target=MARIO,
            prefix=0xF1,
            subscript=[
                ASSetPriority(3),
                ASClearSolidityBits(cant_pass_walls=True),
                ASSequencePlaybackOff(),
                ASShadowOff(),
                ASFaceEast7C(),
                ASAddConstToVar(X_COORD_2, 48),
                ASTransferTo70167018(),
            ]),
        Pause(1),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3143_set_7000_to_70A0_short_mem_1"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO051_MOVING_YELLOW_SWITCH, channel=4),
                ASSetSolidityBits(cant_pass_walls=True),
            ]),
        SetVarToConst(TEMP_7034, 0),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        StartLoopNTimes(47),
        JmpIfMarioInAir(["EVENT_3143_enable_controls_until_return_54"]),
        Pause(1),
        EndLoop(),
        JmpIfMarioInAir(["EVENT_3143_enable_controls_until_return_54"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO051_MOVING_YELLOW_SWITCH, channel=4),
                ASClearSolidityBits(cant_pass_walls=True),
            ]),
        Jmp(["EVENT_3143_set_7000_to_70A0_short_mem_1"]),
        EnableControlsUntilReturn(
            [LEFT, RIGHT, DOWN, UP, X, A, Y, B],
            identifier="EVENT_3143_enable_controls_until_return_54"),
        CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
        EnableObjectTrigger(MEM_70AA),
        UnfreezeCamera(),
        StartSyncEmbeddedActionScript(
            target=SCREEN_FOCUS, prefix=0xF1, subscript=[ASSetWalkingSpeed(NORMAL)]
        ),
        StartSyncEmbeddedActionScript(
            target=MEM_70AA,
            prefix=0xF1,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
            ]),
        SetVarToConst(TEMP_70AA, 0),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSequencePlaybackOn(),
                ASObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
                ASSetSolidityBits(cant_pass_walls=True),
                ASShadowOn(),
            ]),
        Return(),
    ]
)
