# pylint: disable=C0301

"""E3365_KEEP_LOGIC_GAME_FINALIZE_ANSWER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ResumeActionScript(MEM_70A8),
        ClearBit(TEMP_7044_7),
        SetSyncActionScript(
            NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
        ),
        JmpIfVarEqualsConst(TEMP_70AE, 4, ["EVENT_3365_run_dialog_11"]),
        JmpIfVarEqualsConst(TEMP_70AF, 1, ["EVENT_3365_run_dialog_7"]),
        RunDialog(
            dialog_id=DI1932_MARATHON_PROMPT_TO_ENTER,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        JmpIfDialogOptionBSelected(["EVENT_3365_set_bit_9"]),
        RunDialog(
            dialog_id=DI1933_MARATHON_PHASE_2_BEGIN,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
            identifier="EVENT_3365_run_dialog_7"),
        SetVarToConst(TEMP_70AF, 1),
        SetBit(TEMP_7044_7, identifier="EVENT_3365_set_bit_9"),
        Return(),
        RunDialog(
            dialog_id=DI1935_MARATHON_CONFIRM_ORDER,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False,
            identifier="EVENT_3365_run_dialog_11"),
        SetVarToConst(TEMP_7034, 1),
        CopyVarToVar(
            from_var=TEMP_702C,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3365_set_7000_to_7000_short_mem_13"),
        Compare7000ToVar(TEMP_7034),
        JmpIfLoadedMemoryIsNot0(["EVENT_3365_set_7000_to_7000_short_mem_18"]),
        RunDialog(
            dialog_id=DI1921_BOO,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        Jmp(["EVENT_3365_inc_short_32"]),
        CopyVarToVar(
            from_var=TEMP_702E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3365_set_7000_to_7000_short_mem_18"),
        Compare7000ToVar(TEMP_7034),
        JmpIfLoadedMemoryIsNot0(["EVENT_3365_set_7000_to_7000_short_mem_23"]),
        RunDialog(
            dialog_id=DI1922_GOO,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        Jmp(["EVENT_3365_inc_short_32"]),
        CopyVarToVar(
            from_var=TEMP_7030,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3365_set_7000_to_7000_short_mem_23"),
        Compare7000ToVar(TEMP_7034),
        JmpIfLoadedMemoryIsNot0(["EVENT_3365_set_7000_to_7000_short_mem_28"]),
        RunDialog(
            dialog_id=DI1923_BONES,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        Jmp(["EVENT_3365_inc_short_32"]),
        CopyVarToVar(
            from_var=TEMP_7032,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3365_set_7000_to_7000_short_mem_28"),
        Compare7000ToVar(TEMP_7034),
        JmpIfLoadedMemoryIsNot0(["EVENT_3365_inc_short_32"]),
        RunDialog(
            dialog_id=DI1924_KIPP,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        Inc(TEMP_7034, identifier="EVENT_3365_inc_short_32"),
        CompareVarToConst(TEMP_7034, 5),
        JmpIfLoadedMemoryIs0(["EVENT_3365_mem_compare_36"]),
        RunDialog(
            dialog_id=DI1936_MARATHON_CONFIRM_ORDER,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        CompareVarToConst(TEMP_7034, 5, identifier="EVENT_3365_mem_compare_36"),
        JmpIfLoadedMemoryIsNot0(["EVENT_3365_set_7000_to_7000_short_mem_13"]),
        RunDialog(
            dialog_id=DI1937_MARATHON_CONFIRM_ORDER,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        SetBit(TEMP_7044_7),
        JmpIfDialogOptionBSelected(["EVENT_3365_clear_bit_42"]),
        Jmp(["EVENT_3365_set_7000_to_7000_short_mem_49"]),
        ClearBit(TEMP_7043_1, identifier="EVENT_3365_clear_bit_42"),
        ClearBit(TEMP_7043_2),
        ClearBit(TEMP_7043_3),
        ClearBit(TEMP_7043_4),
        SetVarToConst(TEMP_70AE, 0),
        SetVarToConst(TEMP_70AF, 0),
        Return(),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3365_set_7000_to_7000_short_mem_49"),
        Compare7000ToVar(TEMP_702C),
        JmpIfLoadedMemoryIsNot0(["EVENT_3365_play_sound_78"]),
        CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
        Compare7000ToVar(TEMP_702E),
        JmpIfLoadedMemoryIsNot0(["EVENT_3365_play_sound_78"]),
        CopyVarToVar(from_var=TEMP_7028, to_var=PRIMARY_TEMP_7000),
        Compare7000ToVar(TEMP_7030),
        JmpIfLoadedMemoryIsNot0(["EVENT_3365_play_sound_78"]),
        CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
        Compare7000ToVar(TEMP_7032),
        JmpIfLoadedMemoryIsNot0(["EVENT_3365_play_sound_78"]),
        Pause(8),
        ClearBit(TEMP_7044_7),
        SetSyncActionScript(
            NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
        ),
        PlaySound(sound=SO087_CORRECT_SIGNAL, channel=4),
        Pause(16),
        PlayMusicAtDefaultVolume(M09_VICTORY),
        SetBit(TEMP_7044_7),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASStartLoopNTimes(
                    3,
                    identifier="EVENT_3365_action_queue_async_69_SUBSCRIPT_start_loop_n_times_0"),
                ASVisibilityOff(),
                ASPause(2),
                ASVisibilityOn(),
                ASPause(2),
                ASEndLoop(),
                ASVisibilityOff(),
                ASClearSolidityBits(bit_4=True, cant_walk_through=True),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASEndAll(),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASJmp(
                    ["EVENT_3365_action_queue_async_69_SUBSCRIPT_start_loop_n_times_0"]
                )
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASPause(2),
                ASJmp(
                    ["EVENT_3365_action_queue_async_69_SUBSCRIPT_start_loop_n_times_0"]
                ),
            ]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASPause(8),
                ASJmp(
                    ["EVENT_3365_action_queue_async_69_SUBSCRIPT_start_loop_n_times_0"]
                ),
            ]),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASPause(12),
                ASJmp(
                    ["EVENT_3365_action_queue_async_69_SUBSCRIPT_start_loop_n_times_0"]
                ),
            ]),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R466_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1C_WORD_PROBLEM,
            mod_id=0),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R466_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1C_WORD_PROBLEM,
            mod_id=0),
        Return(),
        PlaySound(
            sound=SO088_WRONG_SIGNAL, channel=4, identifier="EVENT_3365_play_sound_78"
        ),
        Pause(16),
        PlayMusicAtDefaultVolume(M66_BOWSERS_CASTLE_2ND_TIME),
        SlowDownMusic(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=12, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(2),
            ]),
        ClearBit(TEMP_7044_7),
        SetSyncActionScript(
            NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
        ),
        RunDialog(
            dialog_id=DI1939_MARATHON_FAIL,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        SetVarToConst(TEMP_7034, 1),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3365_set_7000_to_7000_short_mem_87"),
        Compare7000ToVar(TEMP_7034),
        JmpIfLoadedMemoryIsNot0(["EVENT_3365_set_7000_to_7000_short_mem_92"]),
        RunDialog(
            dialog_id=DI1921_BOO,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        Jmp(["EVENT_3365_inc_short_106"]),
        CopyVarToVar(
            from_var=TEMP_7026,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3365_set_7000_to_7000_short_mem_92"),
        Compare7000ToVar(TEMP_7034),
        JmpIfLoadedMemoryIsNot0(["EVENT_3365_set_7000_to_7000_short_mem_97"]),
        RunDialog(
            dialog_id=DI1922_GOO,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        Jmp(["EVENT_3365_inc_short_106"]),
        CopyVarToVar(
            from_var=TEMP_7028,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3365_set_7000_to_7000_short_mem_97"),
        Compare7000ToVar(TEMP_7034),
        JmpIfLoadedMemoryIsNot0(["EVENT_3365_set_7000_to_7000_short_mem_102"]),
        RunDialog(
            dialog_id=DI1923_BONES,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        Jmp(["EVENT_3365_inc_short_106"]),
        CopyVarToVar(
            from_var=TEMP_702A,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3365_set_7000_to_7000_short_mem_102"),
        Compare7000ToVar(TEMP_7034),
        JmpIfLoadedMemoryIsNot0(["EVENT_3365_inc_short_106"]),
        RunDialog(
            dialog_id=DI1924_KIPP,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        Inc(TEMP_7034, identifier="EVENT_3365_inc_short_106"),
        CompareVarToConst(TEMP_7034, 5),
        JmpIfLoadedMemoryIs0(["EVENT_3365_mem_compare_110"]),
        RunDialog(
            dialog_id=DI1936_MARATHON_CONFIRM_ORDER,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        CompareVarToConst(TEMP_7034, 5, identifier="EVENT_3365_mem_compare_110"),
        JmpIfLoadedMemoryIsNot0(["EVENT_3365_set_7000_to_7000_short_mem_87"]),
        RunDialog(
            dialog_id=DI1940_MARATHON_SUCCESS,
            above_object=NPC_14,
            closable=False,
            sync=True,
            multiline=True,
            use_background=False),
        SetBit(TEMP_7044_7),
        Pause(180),
        FadeOutToBlack(sync=False),
        JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE),
    ]
)
