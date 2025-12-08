# pylint: disable=C0301

"""E3355_KEEP_BARREL_COUNT_LOADER_CONTD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_7044_7),
        SetSyncActionScript(
            NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
        ),
        SetVarToRandom(PRIMARY_TEMP_7000, 256),
        SetVarToRandom(PRIMARY_TEMP_7000, 256),
        SetBit(TEMP_7044_7),
        Db(bytearray(b"\xfd\x8e\x00\x02\x07")),
        Pause(8),
        SetVarToConst(SECONDARY_TEMP_7024, 12),
        SetVarToConst(TEMP_7026, 22),
        SetVarToConst(TEMP_7028, 4),
        JmpToSubroutine(["EVENT_3355_set_7000_to_7000_short_mem_84"]),
        RunDialog(
            dialog_id=DI1888_BARREL_COUNT_1_START,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        Db(bytearray(b"\xfd\x8e2\x02\x07")),
        SetVarToConst(PRIMARY_TEMP_7000, 9),
        JmpToSubroutine(["EVENT_3355_play_music_default_volume_93"]),
        Db(bytearray(b"\xfd\x8e\x00\x02\x07")),
        JmpToSubroutine(["EVENT_3355_clear_bit_111"]),
        JmpIfBitSet(TEMP_7044_6, ["EVENT_3355_play_sound_28"]),
        JmpIfVarEqualsConst(
            ROSE_WAY_703E, 2, ["EVENT_3355_jmp_if_dialog_option_b_or_c_24"]
        ),
        JmpIfVarEqualsConst(
            ROSE_WAY_703E, 3, ["EVENT_3355_jmp_if_dialog_option_b_or_c_26"]
        ),
        JmpIfDialogOptionBOrCSelected(
            ["EVENT_3355_play_sound_28", "EVENT_3355_play_sound_28"]
        ),
        Jmp(["EVENT_3355_pause_38"]),
        JmpIfDialogOptionBOrCSelected(
            ["EVENT_3355_pause_38", "EVENT_3355_play_sound_28"],
            identifier="EVENT_3355_jmp_if_dialog_option_b_or_c_24"),
        Jmp(["EVENT_3355_play_sound_28"]),
        JmpIfDialogOptionBOrCSelected(
            ["EVENT_3355_play_sound_28", "EVENT_3355_pause_38"],
            identifier="EVENT_3355_jmp_if_dialog_option_b_or_c_26"),
        Jmp(["EVENT_3355_play_sound_28"]),
        PlaySound(
            sound=SO088_WRONG_SIGNAL, channel=4, identifier="EVENT_3355_play_sound_28"
        ),
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
            dialog_id=DI1887_QUIZ_FAILED,
            above_object=NPC_14,
            closable=True,
            sync=True,
            multiline=True,
            use_background=False),
        SetBit(TEMP_7044_7),
        Pause(240),
        FadeOutToBlack(sync=False),
        JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE),
        Pause(4, identifier="EVENT_3355_pause_38"),
        PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
        ClearBit(TEMP_7044_7),
        SetSyncActionScript(
            NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
        ),
        Db(bytearray(b"\xfd\x8e\x00\x02\x07")),
        SetBit(TEMP_7044_7),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASVisibilityOn(),
                ASFixedFCoordOn(),
                ASFloatingOn(),
                ASJumpToHeight(0),
                ASPause(40),
                ASWalkNortheastPixels(4),
                ASWalk1StepNortheast(),
                ASPause(20),
                ASFloatingOff(),
                ASShiftZUpSteps(8),
                ASWalkToXYCoords(x=11, y=42),
            ]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(40),
                ASJumpToHeight(56),
                ASSetSpriteSequence(
                    index=9,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
                ASPause(48),
                ASResetProperties(),
            ]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASStartLoopNTimes(4),
                ASVisibilityOff(),
                ASPause(4),
                ASVisibilityOn(),
                ASPause(4),
                ASEndLoop(),
                ASVisibilityOff(),
                ASPause(120),
                ASClearSolidityBits(cant_pass_walls=True),
                ASTransferToXYZF(x=13, y=39, z=16, direction=EAST),
                ASSetSolidityBits(cant_pass_walls=True),
                ASStartLoopNTimes(4),
                ASVisibilityOn(),
                ASPause(4),
                ASVisibilityOff(),
                ASPause(4),
                ASEndLoop(),
                ASVisibilityOn(),
            ]),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASWalk1StepNortheast(),
                ASSetWalkingSpeed(NORMAL),
                ASWalk1StepNortheast(),
                ASSetWalkingSpeed(SLOW),
                ASShiftZUpSteps(2),
            ]),
        Pause(8),
        SetVarToConst(SECONDARY_TEMP_7024, 43),
        SetVarToConst(TEMP_7026, 26),
        SetVarToConst(TEMP_7028, 4),
        JmpToSubroutine(["EVENT_3355_set_7000_to_7000_short_mem_84"]),
        RunDialog(
            dialog_id=DI1896_BARREL_COUNT_2_START,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        Db(bytearray(b"\xfd\x8e2\x02\x07")),
        SetVarToConst(PRIMARY_TEMP_7000, 19),
        JmpToSubroutine(["EVENT_3355_play_music_default_volume_93"]),
        Db(bytearray(b"\xfd\x8e\x00\x02\x07")),
        JmpToSubroutine(["EVENT_3355_clear_bit_111"]),
        JmpIfBitSet(TEMP_7044_6, ["EVENT_3355_play_sound_28"]),
        JmpIfVarEqualsConst(
            ROSE_WAY_703E, 2, ["EVENT_3355_jmp_if_dialog_option_b_or_c_65"]
        ),
        JmpIfVarEqualsConst(
            ROSE_WAY_703E, 3, ["EVENT_3355_jmp_if_dialog_option_b_or_c_67"]
        ),
        JmpIfDialogOptionBOrCSelected(
            ["EVENT_3355_play_sound_28", "EVENT_3355_play_sound_28"]
        ),
        Jmp(["EVENT_3355_pause_69"]),
        JmpIfDialogOptionBOrCSelected(
            ["EVENT_3355_pause_69", "EVENT_3355_play_sound_28"],
            identifier="EVENT_3355_jmp_if_dialog_option_b_or_c_65"),
        Jmp(["EVENT_3355_play_sound_28"]),
        JmpIfDialogOptionBOrCSelected(
            ["EVENT_3355_play_sound_28", "EVENT_3355_pause_69"],
            identifier="EVENT_3355_jmp_if_dialog_option_b_or_c_67"),
        Jmp(["EVENT_3355_play_sound_28"]),
        Pause(4, identifier="EVENT_3355_pause_69"),
        PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
        Pause(8),
        ClearBit(TEMP_7044_7),
        SetSyncActionScript(
            NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
        ),
        PlayMusicAtDefaultVolume(M09_VICTORY),
        SetBit(TEMP_7044_7),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASStartLoopNTimes(3),
                ASVisibilityOff(),
                ASPause(2),
                ASVisibilityOn(),
                ASPause(2),
                ASEndLoop(),
                ASVisibilityOff(),
            ]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASWalk1StepSoutheast(),
                ASWalkNortheastSteps(7),
                ASWalk1StepSoutheast(),
            ]),
        PlaySound(sound=SO016_OPEN_DOOR, channel=4),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R463_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1B_BARRELCOUNTING,
            mod_id=0),
        ActionQueueAsync(
            target=MARIO, subscript=[ASJumpToHeight(48), ASWalk1StepNortheast()]
        ),
        JmpToEvent(E1951_KEEP_BARREL_COUNT_ROOM_EXIT_CONTAINER),
        Return(),
        CopyVarToVar(
            from_var=TEMP_7026,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3355_set_7000_to_7000_short_mem_84"),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        SetObjectMemoryToVar(TEMP_7028),
        JmpIfRandom1of2(["EVENT_3355_end_loop_91"]),
        SetSyncActionScript(MEM_70A9, A0279_KEEP_BARREL_COUNTING_OPTIONAL_BARREL),
        Inc(SECONDARY_TEMP_7024),
        Inc(TEMP_70A9),
        EndLoop(identifier="EVENT_3355_end_loop_91"),
        Return(),
        PlayMusicAtDefaultVolume(
            M36_EXPLANATION, identifier="EVENT_3355_play_music_default_volume_93"
        ),
        CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=TEMP_702A),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
        ActionQueueSync(target=MARIO, subscript=[ASFaceNorthwest(), ASPause(1)]),
        Pause(30),
        RunBackgroundEvent(
            event_id=E1653_EXIT_BARREL_COUNT_TIMER, return_on_level_exit=True
        ),
        SetObjectMemoryToVar(SECONDARY_TEMP_7024),
        JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 0, ["EVENT_3355_end_loop_105"]),
        Pause(30),
        PlaySound(sound=SO144_CLICK, channel=4),
        ClearBit(TEMP_7044_7),
        SetSyncActionScript(
            NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
        ),
        JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 0, ["EVENT_3355_end_loop_105"]),
        RunDialog(
            dialog_id=DI1891_X_SECONDS_LEFT,
            above_object=NPC_14,
            closable=False,
            sync=True,
            multiline=False,
            use_background=False),
        Pause(30),
        SetBit(TEMP_7044_7),
        JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 0, ["EVENT_3355_end_loop_105"]),
        Dec(SECONDARY_TEMP_7024),
        EndLoop(identifier="EVENT_3355_end_loop_105"),
        StopAllBackgroundEvents(),
        Pause(30),
        PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=4),
        ActionQueueSync(target=MARIO, subscript=[ASFaceNortheast(), ASPause(1)]),
        CopyVarToVar(from_var=TEMP_702A, to_var=SECONDARY_TEMP_7024),
        PlayMusicAtDefaultVolume(M66_BOWSERS_CASTLE_2ND_TIME),
        Return(),
        ClearBit(TEMP_7044_7, identifier="EVENT_3355_clear_bit_111"),
        SetSyncActionScript(
            NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
        ),
        RunDialog(
            dialog_id=DI1892_PROMPT_FOR_BARREL_ANSWER,
            above_object=NPC_14,
            closable=False,
            sync=True,
            multiline=True,
            use_background=False),
        PauseScriptResumeOnNextDialogPageB(),
        SetBit(TEMP_7044_7),
        CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
        SetVarToConst(ROSE_WAY_703E, 0),
        JmpIfRandom2of3(["EVENT_3355_inc_short_121", "EVENT_3355_inc_short_123"]),
        Inc(ROSE_WAY_703E),
        Dec(PRIMARY_TEMP_7000),
        Inc(ROSE_WAY_703E, identifier="EVENT_3355_inc_short_121"),
        Dec(PRIMARY_TEMP_7000),
        Inc(ROSE_WAY_703E, identifier="EVENT_3355_inc_short_123"),
        RunDialog(
            dialog_id=DI1893_DUPLICATE,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        Inc(PRIMARY_TEMP_7000),
        RunDialog(
            dialog_id=DI1893_DUPLICATE,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        Inc(PRIMARY_TEMP_7000),
        RunDialog(
            dialog_id=DI1893_DUPLICATE,
            above_object=NPC_14,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        RunDialog(
            dialog_id=DI1894_EMPTY,
            above_object=NPC_14,
            closable=True,
            sync=True,
            multiline=True,
            use_background=False),
        ClearBit(TEMP_7044_6),
        SetVarToConst(TEMP_7028, 30),
        StartLoopNFrames(299),
        Pause(1),
        SetVarToRandom(PRIMARY_TEMP_7000, 256),
        Inc(TEMP_7028),
        JmpIfVarNotEqualsConst(
            TEMP_7028, 60, ["EVENT_3355_if_0210_bits_012_clear_do_not_jump_139"]
        ),
        PlaySound(sound=SO144_CLICK, channel=4),
        SetVarToConst(TEMP_7028, 0),
        If0210Bits012ClearDoNotJump(
            ["EVENT_3355_end_loop_141"],
            identifier="EVENT_3355_if_0210_bits_012_clear_do_not_jump_139"),
        Jmp(["EVENT_3355_close_dialog_143"]),
        EndLoop(identifier="EVENT_3355_end_loop_141"),
        SetBit(TEMP_7044_6),
        CloseDialog(identifier="EVENT_3355_close_dialog_143"),
        Db(bytearray(b"\xfd\x8e2\x02\x07")),
        Return(),
    ]
)
