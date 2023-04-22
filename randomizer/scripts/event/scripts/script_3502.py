# pylint: disable=C0301

"""E3502_BOOSTER_HILL_END"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControlsUntilReturn([B]),
        MoveScriptToBackgroundThread2(),
        Pause(1, identifier="EVENT_3502_pause_2"),
        JmpIfBitSet(
            TEMP_7043_4,
            ["EVENT_3502_move_script_to_main_thread_32"],
            identifier="EVENT_3502_jmp_if_bit_set_3",
        ),
        Set7000ToPressedButton(),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_3502_jmp_if_var_equals_const_24"]
        ),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_3502_jmp_if_var_equals_const_24"]
        ),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_3502_jmp_if_var_equals_const_28"]
        ),
        JmpIf7000AnyBitsSet(
            bits=[], destinations=["EVENT_3502_jmp_if_var_equals_const_28"]
        ),
        Pause(1, identifier="EVENT_3502_pause_9"),
        JmpIfBitSet(
            TEMP_7043_4,
            ["EVENT_3502_move_script_to_main_thread_32"],
            identifier="EVENT_3502_jmp_if_bit_set_10",
        ),
        JmpIfBitClear(TEMP_7043_5, ["EVENT_3502_pause_2"]),
        CompareVarToConst(SECONDARY_TEMP_7024, 0),
        JmpIfLoadedMemoryIs0(["EVENT_3502_clear_bit_22"]),
        JmpIfLoadedMemoryIsAboveOrEqual0(["EVENT_3502_action_queue_async_20"]),
        Dec(TEMP_7026),
        JmpIfVarNotEqualsConst(TEMP_7026, 0, ["EVENT_3502_pause_2"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASWalkSoutheastPixels(1),
                ASDec(SECONDARY_TEMP_7024),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
        ),
        SetVarToConst(TEMP_7026, 1),
        Jmp(["EVENT_3502_jmp_if_bit_set_3"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASWalkNorthwestPixels(1),
                ASInc(SECONDARY_TEMP_7024),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
            identifier="EVENT_3502_action_queue_async_20",
        ),
        Jmp(["EVENT_3502_jmp_if_bit_set_3"]),
        ClearBit(TEMP_7043_5, identifier="EVENT_3502_clear_bit_22"),
        Jmp(["EVENT_3502_pause_2"]),
        JmpIfVarEqualsConst(
            TEMP_7034,
            40,
            ["EVENT_3502_pause_9"],
            identifier="EVENT_3502_jmp_if_var_equals_const_24",
        ),
        ActionQueueAsync(
            target=MARIO, subscript=[ASSetWalkingSpeed(FAST), ASWalkNortheastPixels(2)]
        ),
        Inc(TEMP_7034),
        Jmp(["EVENT_3502_jmp_if_bit_set_10"]),
        JmpIfVarEqualsConst(
            TEMP_7034,
            0,
            ["EVENT_3502_pause_9"],
            identifier="EVENT_3502_jmp_if_var_equals_const_28",
        ),
        ActionQueueAsync(
            target=MARIO, subscript=[ASSetWalkingSpeed(FAST), ASWalkSouthwestPixels(2)]
        ),
        Dec(TEMP_7034),
        Jmp(["EVENT_3502_jmp_if_bit_set_10"]),
        MoveScriptToMainThread(identifier="EVENT_3502_move_script_to_main_thread_32"),
        FreezeAllNPCsUntilReturn(),
        StopAllBackgroundEvents(),
        Db(bytearray(b"\xfdD")),
        StopBackgroundEvent(TIMER_701C),
        StopBackgroundEvent(TIMER_701E),
        SetSyncActionScript(LAYER_1, A0161_SEQUENCE_LOOPING_OFF),
        SetSyncActionScript(LAYER_2, A0161_SEQUENCE_LOOPING_OFF),
        SetSyncActionScript(NPC_0, A0161_SEQUENCE_LOOPING_OFF),
        SetSyncActionScript(NPC_1, A0161_SEQUENCE_LOOPING_OFF),
        SetSyncActionScript(NPC_2, A0161_SEQUENCE_LOOPING_OFF),
        ResumeActionScript(NPC_3),
        ResumeActionScript(NPC_4),
        ResumeActionScript(NPC_5),
        StartSyncEmbeddedActionScript(
            target=LAYER_1, prefix=0xF1, subscript=[ASWalkNorthwestSteps(15)]
        ),
        FadeOutMusicToVolume(duration=5, volume=0),
        Db(bytearray(b"\xfdE")),
        EnableControlsUntilReturn([]),
        JmpIfBitSet(BOOSTER_HILL_CLEARED, ["EVENT_3502_apply_tile_mod_121"]),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R054_BOOSTER_HILL_____DUMMY, mod_id=34
        ),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R054_BOOSTER_HILL_____DUMMY, mod_id=33
        ),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R054_BOOSTER_HILL_____DUMMY, mod_id=32
        ),
        StopEmbeddedActionScript(LAYER_1),
        ResetCoords(NPC_7),
        SetAsyncActionScript(NPC_7, A0160_SEQUENCE_LOOPING_ON),
        CopyVarToVar(from_var=BOOSTER_HILL_70B1, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3502_run_dialog_61"]),
        RunDialog(
            dialog_id=DI1189_FLOWER_SCORE_ON_HILL,
            above_object=TOADSTOOL,
            closable=True,
            sync=True,
            multiline=False,
            use_background=False,
        ),
        Jmp(["EVENT_3502_action_queue_sync_62"]),
        RunDialog(
            dialog_id=DI1193_NO_FLOWER_HILL,
            above_object=TOADSTOOL,
            closable=True,
            sync=True,
            multiline=False,
            use_background=False,
            identifier="EVENT_3502_run_dialog_61",
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[
                ASFixedFCoordOff(),
                ASSetAllSpeeds(FAST),
                ASPause(4),
                ASWalkSouthwestSteps(8),
                ASVisibilityOff(),
            ],
            identifier="EVENT_3502_action_queue_sync_62",
        ),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASWalkNorthPixels(4),
                ASSetSpriteSequence(
                    index=4, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASWalkNorthPixels(4),
                ASPause(64),
                ASVisibilityOff(),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetAllSpeeds(FAST),
                ASSequenceLoopingOff(),
                ASFixedFCoordOff(),
                ASBounceToXYWithHeight(x=5, y=54, height=0),
            ],
        ),
        PlayMusicAtCurrentVolume(M37_BOOSTER_HILL_START),
        FadeOutMusicToVolume(duration=3, volume=127),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNorthwest(),
                ASSetSequenceSpeed(FASTER),
                ASSetSpriteSequence(
                    index=7,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(50),
                ASResetProperties(),
                ASSetSequenceSpeed(FAST),
                ASFixedFCoordOn(),
                ASWalk1StepSouthwest(),
                ASPause(10),
                ASWalkNortheastSteps(2),
                ASPause(10),
                ASFixedFCoordOff(),
                ASFaceNorthwest(),
                ASPause(8),
                ASFaceWest(),
                ASPause(8),
                ASWalkSouthwestSteps(5),
            ],
        ),
        UnfreezeCamera(),
        UnsyncDialog(),
        SetBit(BOOSTER_HILL_CLEARED),
        RunEventAsSubroutine(E3508_BOOSTER_HILL_RETURN),
        ExitToWorldMap(area=OW27_BOOSTER_HILL),
        Return(),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R014_BOOSTER_HILL,
            mod_id=34,
            identifier="EVENT_3502_apply_tile_mod_121",
        ),
        ApplyTileModToLevel(use_alternate=True, room_id=R014_BOOSTER_HILL, mod_id=33),
        ApplyTileModToLevel(use_alternate=True, room_id=R014_BOOSTER_HILL, mod_id=32),
        StopEmbeddedActionScript(LAYER_1),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetAllSpeeds(FAST),
                ASSequenceLoopingOff(),
                ASFixedFCoordOff(),
                ASBounceToXYWithHeight(x=5, y=54, height=0),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNorthwest(),
                ASSetSequenceSpeed(FASTER),
                ASSetSpriteSequence(
                    index=7,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(120),
                ASResetProperties(),
                ASWalkSouthwestSteps(5),
            ],
        ),
        UnfreezeCamera(),
        SetBit(MAP_BOOSTER_HILL),
        RunDialog(
            dialog_id=DI1198_HILL_COMPLETED_WHEN_EMPTY,
            above_object=TOADSTOOL,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        ExitToWorldMap(area=OW27_BOOSTER_HILL, bit_6=True, bit_7=True),
        Return(),
    ]
)
