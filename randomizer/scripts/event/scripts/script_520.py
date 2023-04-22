# pylint: disable=C0301

"""E0520_ROSE_TOWN_OCCUPIED_EXTERIOR_PINK_TOAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(FREEZE_ROSE_TOWN_NPC_2, ["EVENT_520_run_dialog_31"]),
        PauseActionScript(NPC_2),
        Db(bytearray(b"\xc7\x96")),
        CopyVarToVar(from_var=X_COORD_2, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70B8),
        CopyVarToVar(from_var=Y_COORD_2, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_TOWN_ARROW_POSITION),
        StartAsyncEmbeddedActionScript(
            target=NPC_2,
            prefix=0xF1,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(SLOW),
                ASRunAwayShift(),
            ],
        ),
        RunDialog(
            dialog_id=DI0788_SOME_JERK_IN_THE_FOREST,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASFixedFCoordOff(),
                ASSetSolidityBits(cant_walk_through=True),
                ASFaceMario(),
            ],
        ),
        JmpIfBitSet(TEMP_7044_3, ["EVENT_520_resume_action_script_27"]),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASDb(bytearray(b"\xfd$\x07\x00")),
                ASMem700CAndConst(0x00C0),
                ASCopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_702A),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    0,
                    ["EVENT_520_action_queue_async_11_SUBSCRIPT_face_northwest_7"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    64,
                    [
                        "EVENT_520_action_queue_async_11_SUBSCRIPT_set_700C_to_object_coord_9"
                    ],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    128,
                    ["EVENT_520_action_queue_async_11_SUBSCRIPT_face_southeast_14"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    192,
                    [
                        "EVENT_520_action_queue_async_11_SUBSCRIPT_set_700C_to_object_coord_9"
                    ],
                ),
                ASFaceNorthwest(
                    identifier="EVENT_520_action_queue_async_11_SUBSCRIPT_face_northwest_7"
                ),
                ASJmp(["EVENT_520_action_queue_sync_12"]),
                ASSet700CToObjectCoord(
                    target_npc=NPC_2,
                    coord=COORD_X,
                    pixel=True,
                    bit_7=True,
                    identifier="EVENT_520_action_queue_async_11_SUBSCRIPT_set_700C_to_object_coord_9",
                ),
                ASCopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_702C),
                ASCompareVarToConst(TEMP_702C, 4),
                ASJmpIfComparisonResultIsGreaterOrEqual(
                    ["EVENT_520_action_queue_async_11_SUBSCRIPT_face_northwest_7"]
                ),
                ASJmp(["EVENT_520_action_queue_async_11_SUBSCRIPT_face_southeast_14"]),
                ASFaceSoutheast(
                    identifier="EVENT_520_action_queue_async_11_SUBSCRIPT_face_southeast_14"
                ),
                ASSetBit(TEMP_7043_0),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASClearSolidityBits(cant_pass_walls=True),
                ASWalk1StepFDirection(),
                ASSet700CToObjectCoord(target_npc=NPC_2, coord=COORD_F, pixel=True),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    5,
                    [
                        "EVENT_520_action_queue_sync_12_SUBSCRIPT_object_memory_clear_bit_6"
                    ],
                ),
                ASSetSpriteSequence(
                    index=10, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASObjectMemoryClearBit(
                    arg_1=0x08,
                    bits=[3, 4],
                    identifier="EVENT_520_action_queue_sync_12_SUBSCRIPT_object_memory_clear_bit_6",
                ),
            ],
            identifier="EVENT_520_action_queue_sync_12",
        ),
        SetAsyncActionScript(NPC_7, A0639_ROSE_TOWN_ARROW_THAT_FREEZES_TOAD_BY_INN),
        RememberLastObject(),
        Db(bytearray(b"\xc7\x96")),
        CopyVarToVar(from_var=X_COORD_2, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70B8),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_520_add_25"]),
        CopyVarToVar(
            from_var=Y_COORD_2,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_520_set_7000_to_7000_short_mem_19",
        ),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_TOWN_ARROW_POSITION),
        SetSyncActionScript(NPC_2, A0015_DO_NOTHING),
        ClearBit(TEMP_7043_0),
        SetBit(FREEZE_ROSE_TOWN_NPC_2),
        Return(),
        AddConstToVar(TEMP_70B8, 128, identifier="EVENT_520_add_25"),
        Jmp(["EVENT_520_set_7000_to_7000_short_mem_19"]),
        ResumeActionScript(NPC_2, identifier="EVENT_520_resume_action_script_27"),
        Return(),
        RunDialog(
            dialog_id=DI0813_CANT_MOVE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_520_run_dialog_31",
        ),
        Return(),
    ]
)
