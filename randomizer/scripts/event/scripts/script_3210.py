# pylint: disable=C0301

"""E3210_SHIP_TRAMPOLINE_PUZZLE_BLOCK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO005_BLOCK_SWITCH, channel=4),
        DisableObjectTrigger(MEM_70A8),
        SetTempSyncActionScript(MEM_70A8, A0337_VARIOUS_SHIP_OBJECTS),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 65533),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 1),
        JmpIfMem704XAt7000BitSet(["EVENT_3210_resume_action_script_82"]),
        PauseActionScript(MEM_70A9),
        SetMem704XAt7000Bit(),
        Set7000ToObjectCoord(target_npc=MEM_70A9, coord=COORD_X, pixel=True),
        JmpIfVarEqualsConst(
            TEMP_70A9, 20, ["EVENT_3210_set_7000_short_mem_to_7000_15"]
        ),
        JmpIfVarEqualsConst(
            TEMP_70A9, 21, ["EVENT_3210_set_7000_short_mem_to_7000_17"]
        ),
        JmpIfVarEqualsConst(
            TEMP_70A9, 22, ["EVENT_3210_set_7000_short_mem_to_7000_19"]
        ),
        CopyVarToVar(
            from_var=PRIMARY_TEMP_7000,
            to_var=SECONDARY_TEMP_7024,
            identifier="EVENT_3210_set_7000_short_mem_to_7000_15"),
        Jmp(["EVENT_3210_jmp_if_bit_clear_21"]),
        CopyVarToVar(
            from_var=PRIMARY_TEMP_7000,
            to_var=TEMP_7026,
            identifier="EVENT_3210_set_7000_short_mem_to_7000_17"),
        Jmp(["EVENT_3210_jmp_if_bit_clear_21"]),
        CopyVarToVar(
            from_var=PRIMARY_TEMP_7000,
            to_var=TEMP_7028,
            identifier="EVENT_3210_set_7000_short_mem_to_7000_19"),
        Jmp(["EVENT_3210_jmp_if_bit_clear_21"]),
        JmpIfBitClear(
            TEMP_7043_0,
            ["EVENT_3210_ret_72"],
            identifier="EVENT_3210_jmp_if_bit_clear_21"),
        JmpIfBitClear(TEMP_7043_1, ["EVENT_3210_ret_72"]),
        JmpIfBitClear(TEMP_7043_2, ["EVENT_3210_ret_72"]),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASBounceToXYWithHeight(x=0, y=103, height=10),
            ]),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASTransferToXYZF(x=2, y=121, z=0, direction=SOUTHEAST),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=False),
                ASSetPaletteRow(5),
                ASVisibilityOn(),
                ASFloatingOn(),
                ASWalkNortheastPixels(
                    1,
                    identifier="EVENT_3210_action_queue_async_25_SUBSCRIPT_shift_northeast_pixels_6"),
                ASJmpIfObjectInAir(
                    DUMMY_0X07,
                    [
                        "EVENT_3210_action_queue_async_25_SUBSCRIPT_shift_northeast_pixels_6"
                    ]),
            ]),
        Set7000ToObjectCoord(target_npc=NPC_7, coord=COORD_X, pixel=True),
        DecVarFrom7000(SECONDARY_TEMP_7024),
        JmpIfLoadedMemoryIsBelow0(["EVENT_3210_mem_compare_val_31"]),
        Mem7000XorConst(0xFFFF),
        Inc(PRIMARY_TEMP_7000),
        CompareVarToConst(
            PRIMARY_TEMP_7000, 192, identifier="EVENT_3210_mem_compare_val_31"
        ),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3210_action_queue_sync_73"]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetSequenceSpeed(VERY_FAST),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=False),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=4),
            ]),
        ActionQueueSync(target=SCREEN_FOCUS, subscript=[ASWalkNortheastSteps(3)]),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASClearSolidityBits(cant_pass_npcs=True),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetWalkingSpeed(VERY_FAST),
                ASFloatingOff(),
                ASShiftZDownPixels(12),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(height=240, silent=True),
                ASFloatingOn(),
                ASSetSolidityBits(cant_pass_npcs=True),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASWalkNortheastPixels(
                    1,
                    identifier="EVENT_3210_action_queue_async_35_SUBSCRIPT_shift_northeast_pixels_10"),
                ASJmpIfObjectInAir(
                    DUMMY_0X07,
                    [
                        "EVENT_3210_action_queue_async_35_SUBSCRIPT_shift_northeast_pixels_10"
                    ]),
            ]),
        Set7000ToObjectCoord(target_npc=NPC_7, coord=COORD_X, pixel=True),
        DecVarFrom7000(TEMP_7026),
        JmpIfLoadedMemoryIsBelow0(["EVENT_3210_mem_compare_val_41"]),
        Mem7000XorConst(0xFFFF),
        Inc(PRIMARY_TEMP_7000),
        CompareVarToConst(
            PRIMARY_TEMP_7000, 192, identifier="EVENT_3210_mem_compare_val_41"
        ),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3210_action_queue_sync_73"]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetSequenceSpeed(VERY_FAST),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=False),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=4),
            ]),
        ActionQueueSync(target=SCREEN_FOCUS, subscript=[ASWalkNortheastSteps(3)]),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASClearSolidityBits(cant_pass_npcs=True),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetWalkingSpeed(VERY_FAST),
                ASFloatingOff(),
                ASShiftZDownPixels(12),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(height=192, silent=True),
                ASFloatingOn(),
                ASSetSolidityBits(cant_pass_npcs=True),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASWalkNortheastPixels(
                    1,
                    identifier="EVENT_3210_action_queue_async_45_SUBSCRIPT_shift_northeast_pixels_10"),
                ASJmpIfObjectInAir(
                    DUMMY_0X07,
                    [
                        "EVENT_3210_action_queue_async_45_SUBSCRIPT_shift_northeast_pixels_10"
                    ]),
            ]),
        Set7000ToObjectCoord(target_npc=NPC_7, coord=COORD_X, pixel=True),
        DecVarFrom7000(TEMP_7028),
        JmpIfLoadedMemoryIsBelow0(["EVENT_3210_mem_compare_val_51"]),
        Mem7000XorConst(0xFFFF),
        Inc(PRIMARY_TEMP_7000),
        CompareVarToConst(
            PRIMARY_TEMP_7000, 192, identifier="EVENT_3210_mem_compare_val_51"
        ),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3210_action_queue_sync_73"]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetSequenceSpeed(VERY_FAST),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=False),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=4),
            ]),
        ActionQueueSync(target=SCREEN_FOCUS, subscript=[ASWalkNortheastSteps(3)]),
        ActionQueueAsync(
            target=NPC_7,
            subscript=[
                ASClearSolidityBits(cant_pass_npcs=True),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetWalkingSpeed(VERY_FAST),
                ASFloatingOff(),
                ASShiftZDownPixels(12),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(height=144, silent=True),
                ASFloatingOn(),
                ASSetSolidityBits(cant_pass_npcs=True),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASWalkNortheastPixels(
                    1,
                    identifier="EVENT_3210_action_queue_async_55_SUBSCRIPT_shift_northeast_pixels_10"),
                ASJmpIfObjectInAir(
                    DUMMY_0X07,
                    [
                        "EVENT_3210_action_queue_async_55_SUBSCRIPT_shift_northeast_pixels_10"
                    ]),
            ]),
        JmpIfObjectsAreLessThanXYStepsApartSameZCoord(
            NPC_7, NPC_6, 0, 1, ["EVENT_3210_set_bit_58"]
        ),
        Jmp(["EVENT_3210_action_queue_sync_73"]),
        SetBit(TEMP_7043_3, identifier="EVENT_3210_set_bit_58"),
        SetSyncActionScript(NPC_3, A0316_SHIP_TRAMPOLINE_PUZZLE_BLOCK_FREEZE),
        SetSyncActionScript(NPC_4, A0316_SHIP_TRAMPOLINE_PUZZLE_BLOCK_FREEZE),
        SetSyncActionScript(NPC_5, A0316_SHIP_TRAMPOLINE_PUZZLE_BLOCK_FREEZE),
        Pause(8),
        SetSyncActionScript(NPC_8, A0338_SHIP_TRAMPOLINE_PUZZLE_SCROLL),
        JmpIfBitSet(UNKNOWN_707D_1, ["EVENT_3210_action_queue_async_71"]),
        SetVarToConst(X_COORD_1, 6),
        SetVarToConst(Y_COORD_1, 120),
        SetVarToConst(Z_COORD_1, 16),
        Db(bytearray(b"\xfd\xc4")),
        Pause(1, identifier="EVENT_3210_pause_69"),
        JmpToEvent(E3383_SHIP_TRAMPOLINE_PRIZE_PACKET_GRANT),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASDb(bytearray(b"\xc8\x80")),
                ASAddConstToVar(X_COORD_2, 65532),
                ASCompareVarToConst(X_COORD_2, 0),
                ASJmpIfLoadedMemoryIsBelow0(
                    ["EVENT_3210_action_queue_async_71_SUBSCRIPT_add_short_5"]
                ),
                ASSetVarToConst(X_COORD_2, 0),
                ASAddConstToVar(
                    Y_COORD_2,
                    65520,
                    identifier="EVENT_3210_action_queue_async_71_SUBSCRIPT_add_short_5"),
                ASDb(bytearray(b"\x98")),
                ASSetWalkingSpeed(NORMAL),
            ],
            identifier="EVENT_3210_action_queue_async_71"),
        Return(identifier="EVENT_3210_ret_72"),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASJumpToHeight(height=64, silent=True),
                ASPause(20),
                ASJumpToHeight(height=32, silent=True),
                ASPause(10),
                ASJumpToHeight(height=8, silent=True),
                ASPause(8),
                ASVisibilityOff(),
            ],
            identifier="EVENT_3210_action_queue_sync_73"),
        ResumeActionScript(NPC_0),
        ResumeActionScript(NPC_1),
        ResumeActionScript(NPC_2),
        ClearBit(TEMP_7043_0),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7043_2),
        PlaySound(sound=SO088_WRONG_SIGNAL, channel=6),
        Jmp(["EVENT_3210_action_queue_async_71"]),
        ResumeActionScript(MEM_70A9, identifier="EVENT_3210_resume_action_script_82"),
        ClearMem704XAt7000Bit(),
        Return(),
    ]
)
