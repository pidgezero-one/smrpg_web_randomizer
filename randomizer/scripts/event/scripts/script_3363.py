# E3363_KEEP_BALL_SOLITAIRE_KICK_BALL

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSet700CToObjectCoord(object=MARIO, coord=COORD_F, pixel=True),
                ASCopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=ROSE_WAY_7038),
            ],
        ),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 65515),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
        JmpIf7000AnyBitsSet(destinations=["EVENT_3363_jmp_if_7000_any_bits_set_12"]),
        JmpIf7000AnyBitsSet(destinations=["EVENT_3363_jmp_if_var_equals_const_9"]),
        JmpIfVarEqualsConst(
            ROSE_WAY_7038, 7, ["EVENT_3363_set_7000_to_7000_short_mem_19"]
        ),
        JmpIfVarEqualsConst(
            ROSE_WAY_7038, 1, ["EVENT_3363_set_7000_to_7000_short_mem_35"]
        ),
        Jmp(["EVENT_3363_play_sound_153"]),
        JmpIfVarEqualsConst(
            ROSE_WAY_7038,
            1,
            ["EVENT_3363_set_7000_to_7000_short_mem_35"],
            identifier="EVENT_3363_jmp_if_var_equals_const_9",
        ),
        JmpIfVarEqualsConst(
            ROSE_WAY_7038, 3, ["EVENT_3363_set_7000_to_7000_short_mem_53"]
        ),
        Jmp(["EVENT_3363_play_sound_153"]),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3363_jmp_if_var_equals_const_16"],
            identifier="EVENT_3363_jmp_if_7000_any_bits_set_12",
        ),
        JmpIfVarEqualsConst(
            ROSE_WAY_7038, 5, ["EVENT_3363_set_7000_to_7000_short_mem_71"]
        ),
        JmpIfVarEqualsConst(
            ROSE_WAY_7038, 7, ["EVENT_3363_set_7000_to_7000_short_mem_19"]
        ),
        Jmp(["EVENT_3363_play_sound_153"]),
        JmpIfVarEqualsConst(
            ROSE_WAY_7038,
            5,
            ["EVENT_3363_set_7000_to_7000_short_mem_71"],
            identifier="EVENT_3363_jmp_if_var_equals_const_16",
        ),
        JmpIfVarEqualsConst(
            ROSE_WAY_7038, 3, ["EVENT_3363_set_7000_to_7000_short_mem_53"]
        ),
        Jmp(["EVENT_3363_play_sound_153"]),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3363_set_7000_to_7000_short_mem_19",
        ),
        AddConstToVar(PRIMARY_TEMP_7000, 25),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        JmpIfObjectInCurrentLevel(MEM_70A9, ["EVENT_3363_play_sound_153"]),
        AddConstToVar(PRIMARY_TEMP_7000, 4),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        JmpIfObjectInCurrentLevel(
            MEM_70A9, ["EVENT_3363_set_7000_to_7000_short_mem_27"]
        ),
        Jmp(["EVENT_3363_play_sound_153"]),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3363_set_7000_to_7000_short_mem_27",
        ),
        AddConstToVar(PRIMARY_TEMP_7000, 21),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
        AddConstToVar(PRIMARY_TEMP_7000, 4),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        AddConstToVar(PRIMARY_TEMP_7000, 4),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
        Jmp(["EVENT_3363_clear_bit_89"]),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3363_set_7000_to_7000_short_mem_35",
        ),
        AddConstToVar(PRIMARY_TEMP_7000, 22),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        JmpIfObjectInCurrentLevel(MEM_70A9, ["EVENT_3363_play_sound_153"]),
        AddConstToVar(PRIMARY_TEMP_7000, 1),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        JmpIfObjectInCurrentLevel(
            MEM_70A9, ["EVENT_3363_set_7000_to_7000_short_mem_43"]
        ),
        Jmp(["EVENT_3363_play_sound_153"]),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3363_set_7000_to_7000_short_mem_43",
        ),
        AddConstToVar(PRIMARY_TEMP_7000, 21),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
        AddConstToVar(PRIMARY_TEMP_7000, 1),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        AddConstToVar(PRIMARY_TEMP_7000, 1),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7043_2),
        Jmp(["EVENT_3363_clear_bit_89"]),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3363_set_7000_to_7000_short_mem_53",
        ),
        AddConstToVar(PRIMARY_TEMP_7000, 17),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        JmpIfObjectInCurrentLevel(MEM_70A9, ["EVENT_3363_play_sound_153"]),
        AddConstToVar(PRIMARY_TEMP_7000, 65532),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        JmpIfObjectInCurrentLevel(
            MEM_70A9, ["EVENT_3363_set_7000_to_7000_short_mem_61"]
        ),
        Jmp(["EVENT_3363_play_sound_153"]),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3363_set_7000_to_7000_short_mem_61",
        ),
        AddConstToVar(PRIMARY_TEMP_7000, 21),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
        AddConstToVar(PRIMARY_TEMP_7000, 65532),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        AddConstToVar(PRIMARY_TEMP_7000, 65532),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7043_2),
        Jmp(["EVENT_3363_clear_bit_89"]),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3363_set_7000_to_7000_short_mem_71",
        ),
        AddConstToVar(PRIMARY_TEMP_7000, 20),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        JmpIfObjectInCurrentLevel(MEM_70A9, ["EVENT_3363_play_sound_153"]),
        AddConstToVar(PRIMARY_TEMP_7000, 65535),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        JmpIfObjectInCurrentLevel(
            MEM_70A9, ["EVENT_3363_set_7000_to_7000_short_mem_79"]
        ),
        Jmp(["EVENT_3363_play_sound_153"]),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3363_set_7000_to_7000_short_mem_79",
        ),
        AddConstToVar(PRIMARY_TEMP_7000, 21),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
        AddConstToVar(PRIMARY_TEMP_7000, 65535),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        AddConstToVar(PRIMARY_TEMP_7000, 65535),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7043_2),
        Jmp(["EVENT_3363_clear_bit_89"]),
        ClearBit(TEMP_7043_1, identifier="EVENT_3363_clear_bit_89"),
        ClearBit(TEMP_7043_2),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSet700CToObjectCoord(object=DUMMY_0X07, coord=COORD_F, pixel=True),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    7,
                    ["EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_5"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    1,
                    ["EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_7"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    3,
                    ["EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_9"],
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    5,
                    [
                        "EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_11"
                    ],
                ),
                ASSetSpriteSequence(
                    index=9,
                    sprite_offset=1,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                    identifier="EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_5",
                ),
                ASJmp(["EVENT_3363_action_queue_sync_91_SUBSCRIPT_pause_13"]),
                ASSetSpriteSequence(
                    index=8,
                    sprite_offset=1,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                    identifier="EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_7",
                ),
                ASJmp(["EVENT_3363_action_queue_sync_91_SUBSCRIPT_pause_13"]),
                ASSetSpriteSequence(
                    index=8,
                    sprite_offset=1,
                    is_sequence=True,
                    looping=True,
                    identifier="EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_9",
                ),
                ASJmp(["EVENT_3363_action_queue_sync_91_SUBSCRIPT_pause_13"]),
                ASSetSpriteSequence(
                    index=9,
                    sprite_offset=1,
                    is_sequence=True,
                    looping=True,
                    identifier="EVENT_3363_action_queue_sync_91_SUBSCRIPT_set_sprite_sequence_11",
                ),
                ASJmp(["EVENT_3363_action_queue_sync_91_SUBSCRIPT_pause_13"]),
                ASPause(
                    12, identifier="EVENT_3363_action_queue_sync_91_SUBSCRIPT_pause_13"
                ),
                ASResetProperties(),
            ],
        ),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASCopyVarToVar(from_var=ROSE_WAY_7038, to_var=PRIMARY_TEMP_700C),
                ASFaceEast7C(),
                ASDb(bytearray(b"\xc8\x07")),
                ASPlaySound(sound=SO066_KICK_BALL_SHELL, channel=4),
                ASJumpToHeight(height=124, silent=True),
                ASSetSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASShiftFDirectionSteps(2),
                ASSetBit(TEMP_7043_1),
                ASJumpToHeight(height=120, silent=True),
                ASShiftFDirectionSteps(2),
                ASSetBit(TEMP_7043_2),
                ASVisibilityOff(),
                ASDb(bytearray(b"\x99")),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        ActionQueueSync(
            target=MEM_70A9,
            subscript=[
                ASPause(
                    1, identifier="EVENT_3363_action_queue_sync_93_SUBSCRIPT_pause_0"
                ),
                ASJmpIfBitClear(
                    TEMP_7043_1, ["EVENT_3363_action_queue_sync_93_SUBSCRIPT_pause_0"]
                ),
                ASPlaySound(sound=SO022_CLOSE_DOOR, channel=4),
                ASVisibilityOff(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASPause(8),
                ASDb(bytearray(b"\xfd\x9cW")),
                ASEndAll(),
            ],
        ),
        ActionQueueAsync(
            target=MEM_70AA,
            subscript=[
                ASPause(
                    1, identifier="EVENT_3363_action_queue_async_94_SUBSCRIPT_pause_0"
                ),
                ASJmpIfBitClear(
                    TEMP_7043_2, ["EVENT_3363_action_queue_async_94_SUBSCRIPT_pause_0"]
                ),
                ASVisibilityOn(),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASEndAll(),
            ],
        ),
        Dec(ROSE_WAY_703E),
        JmpIfVarEqualsConst(ROSE_WAY_703E, 1, ["EVENT_3363_pause_155"]),
        Jmp(["EVENT_3363_clear_bit_98"]),
        ClearBit(TEMP_7043_0, identifier="EVENT_3363_clear_bit_98"),
        SetVarToConst(SECONDARY_TEMP_7024, 0),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3363_set_7000_to_7000_short_mem_100",
        ),
        AddConstToVar(PRIMARY_TEMP_7000, 21),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        JmpIfObjectInCurrentLevel(MEM_70A9, ["EVENT_3363_inc_short_149"]),
        CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
        JmpIf7000AnyBitsSet(destinations=["EVENT_3363_jmp_if_7000_any_bits_set_113"]),
        JmpIf7000AnyBitsSet(destinations=["EVENT_3363_jmp_to_subroutine_110"]),
        JmpToSubroutine(["EVENT_3363_set_7000_to_7000_short_mem_120"]),
        JmpToSubroutine(["EVENT_3363_set_7000_to_7000_short_mem_126"]),
        Jmp(["EVENT_3363_inc_short_149"]),
        JmpToSubroutine(
            ["EVENT_3363_set_7000_to_7000_short_mem_126"],
            identifier="EVENT_3363_jmp_to_subroutine_110",
        ),
        JmpToSubroutine(["EVENT_3363_set_7000_to_7000_short_mem_132"]),
        Jmp(["EVENT_3363_inc_short_149"]),
        JmpIf7000AnyBitsSet(
            destinations=["EVENT_3363_jmp_to_subroutine_117"],
            identifier="EVENT_3363_jmp_if_7000_any_bits_set_113",
        ),
        JmpToSubroutine(["EVENT_3363_set_7000_to_7000_short_mem_138"]),
        JmpToSubroutine(["EVENT_3363_set_7000_to_7000_short_mem_120"]),
        Jmp(["EVENT_3363_inc_short_149"]),
        JmpToSubroutine(
            ["EVENT_3363_set_7000_to_7000_short_mem_138"],
            identifier="EVENT_3363_jmp_to_subroutine_117",
        ),
        JmpToSubroutine(["EVENT_3363_set_7000_to_7000_short_mem_132"]),
        Jmp(["EVENT_3363_inc_short_149"]),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3363_set_7000_to_7000_short_mem_120",
        ),
        AddConstToVar(PRIMARY_TEMP_7000, 25),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        AddConstToVar(PRIMARY_TEMP_7000, 4),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
        Jmp(["EVENT_3363_jmp_if_present_in_current_level_144"]),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3363_set_7000_to_7000_short_mem_126",
        ),
        AddConstToVar(PRIMARY_TEMP_7000, 22),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        AddConstToVar(PRIMARY_TEMP_7000, 1),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
        Jmp(["EVENT_3363_jmp_if_present_in_current_level_144"]),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3363_set_7000_to_7000_short_mem_132",
        ),
        AddConstToVar(PRIMARY_TEMP_7000, 17),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        AddConstToVar(PRIMARY_TEMP_7000, 65532),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
        Jmp(["EVENT_3363_jmp_if_present_in_current_level_144"]),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3363_set_7000_to_7000_short_mem_138",
        ),
        AddConstToVar(PRIMARY_TEMP_7000, 20),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
        AddConstToVar(PRIMARY_TEMP_7000, 65535),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
        Jmp(["EVENT_3363_jmp_if_present_in_current_level_144"]),
        JmpIfObjectInCurrentLevel(
            MEM_70A9,
            ["EVENT_3363_ret_146"],
            identifier="EVENT_3363_jmp_if_present_in_current_level_144",
        ),
        JmpIfObjectInCurrentLevel(MEM_70AA, ["EVENT_3363_set_bit_147"]),
        Return(identifier="EVENT_3363_ret_146"),
        SetBit(TEMP_7043_0, identifier="EVENT_3363_set_bit_147"),
        Return(),
        Inc(SECONDARY_TEMP_7024, identifier="EVENT_3363_inc_short_149"),
        JmpIfVarNotEqualsConst(
            SECONDARY_TEMP_7024, 16, ["EVENT_3363_set_7000_to_7000_short_mem_100"]
        ),
        JmpIfBitClear(TEMP_7043_0, ["EVENT_3363_play_sound_168"]),
        Return(),
        PlaySound(
            sound=SO088_WRONG_SIGNAL, channel=4, identifier="EVENT_3363_play_sound_153"
        ),
        Return(),
        Pause(8, identifier="EVENT_3363_pause_155"),
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
                ASStartLoopNTimes(3),
                ASVisibilityOff(),
                ASPause(2),
                ASVisibilityOn(),
                ASPause(2),
                ASEndLoop(),
                ASVisibilityOff(),
                ASClearSolidityBits(bit_4=True, cant_walk_through=True),
            ],
        ),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R468_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2C_BALL_SOLITAIRE,
            mod_id=0,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R468_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2C_BALL_SOLITAIRE,
            mod_id=0,
        ),
        Return(),
        PlaySound(
            sound=SO088_WRONG_SIGNAL, channel=4, identifier="EVENT_3363_play_sound_168"
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
            ],
        ),
        ClearBit(TEMP_7044_7),
        SetSyncActionScript(
            NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
        ),
        RunDialog(
            dialog_id=DI1915_MINIGAME_LOSE,
            above_object=NPC_14,
            closable=True,
            sync=True,
            multiline=True,
            use_background=False,
        ),
        SetBit(TEMP_7044_7),
        Pause(180),
        FadeOutToBlack(sync=False),
        JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE),
    ]
)
