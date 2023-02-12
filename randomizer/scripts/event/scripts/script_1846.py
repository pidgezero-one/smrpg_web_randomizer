# E1846_SAFE_DONUT_LIFT_JUMP

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            TEMP_7043_1,
            ["EVENT_1846_clear_bit_30"],
            identifier="EVENT_1846_jmp_if_bit_set_0",
        ),
        EnableControls([B]),
        MoveScriptToBackgroundThread2(),
        SetBit(TEMP_7043_1),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO058_INSERT, channel=4),
                ASSet700CToObjectCoord(object=MARIO, coord=COORD_F, pixel=True),
                ASCopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_702A),
                ASDb(bytearray(b"\xc8\x91")),
                ASSetWalkingSpeed(FAST),
                ASFloatingOff(),
                ASRunAwayShift(),
                ASFloatingOn(),
                ASSetWalkingSpeed(NORMAL),
                ASCopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_700C),
                ASFaceEast7C(),
            ],
        ),
        Set7000ToTappedButton(identifier="EVENT_1846_set_7000_to_tapped_button_7"),
        JmpIf7000AnyBitsSet(destinations=["EVENT_1846_action_queue_sync_21"]),
        JmpIfMarioInAir(["EVENT_1846_clear_bit_30"]),
        Set7000ToPressedButton(),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=X_COORD_1),
        JmpIf7000AnyBitsSet(destinations=["EVENT_1846_action_queue_sync_17"]),
        CopyVarToVar(from_var=X_COORD_1, to_var=PRIMARY_TEMP_7000),
        JmpIf7000AnyBitsSet(destinations=["EVENT_1846_action_queue_sync_19"]),
        Pause(1, identifier="EVENT_1846_pause_15"),
        Jmp(["EVENT_1846_set_7000_to_tapped_button_7"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[ASFaceNorthwest()],
            identifier="EVENT_1846_action_queue_sync_17",
        ),
        Jmp(["EVENT_1846_pause_15"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[ASFaceSoutheast()],
            identifier="EVENT_1846_action_queue_sync_19",
        ),
        Jmp(["EVENT_1846_pause_15"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[ASJumpToHeight(108)],
            identifier="EVENT_1846_action_queue_sync_21",
        ),
        StartLoopNTimes(11),
        Pause(1),
        Set7000ToPressedButton(),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=X_COORD_1),
        JmpIf7000AnyBitsSet(destinations=["EVENT_1846_set_7000_to_70A0_short_mem_33"]),
        CopyVarToVar(from_var=X_COORD_1, to_var=PRIMARY_TEMP_7000),
        JmpIf7000AnyBitsSet(destinations=["EVENT_1846_action_queue_async_39"]),
        EndLoop(),
        ClearBit(TEMP_7043_1, identifier="EVENT_1846_clear_bit_30"),
        MoveScriptToMainThread(),
        Return(),
        CopyVarToVar(
            from_var=ACTIVE_NPC,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_1846_set_7000_to_70A0_short_mem_33",
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 23, ["EVENT_1846_action_queue_async_37"]
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASShiftNorthwestSteps(2),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        Jmp(["EVENT_1846_clear_bit_30"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FASTER),
                ASShiftNorthwestSteps(3),
                ASSetWalkingSpeed(NORMAL),
            ],
            identifier="EVENT_1846_action_queue_async_37",
        ),
        Jmp(["EVENT_1846_clear_bit_30"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASShiftSoutheastSteps(2),
                ASSetWalkingSpeed(NORMAL),
            ],
            identifier="EVENT_1846_action_queue_async_39",
        ),
        Jmp(["EVENT_1846_clear_bit_30"]),
    ]
)
