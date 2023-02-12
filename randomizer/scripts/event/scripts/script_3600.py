# E3600_MUSHROOM_DERBY_GOAL_TILE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MUSHROOM_DERBY_AUTO, ["EVENT_3584_ret_0"]),
        JmpIfBitClear(UNKNOWN_MUSHROOM_DERBY_7085_4, ["EVENT_3584_ret_0"]),
        ClearBit(UNKNOWN_MUSHROOM_DERBY_7085_4),
        FreezeCamera(),
        StopAllBackgroundEvents(),
        Db(bytearray(b"\xfdD")),
        Db(bytearray(b"\xfdE")),
        PauseActionScript(MARIO),
        StartSyncEmbeddedActionScript(
            target=MARIO,
            prefix=0xF1,
            subscript=[ASBPL262728(), ASWalkToXYCoords(x=20, y=61)],
        ),
        CloseDialog(),
        PauseActionScript(NPC_9),
        StartAsyncEmbeddedActionScript(
            target=NPC_9,
            prefix=0xF1,
            subscript=[
                ASResetProperties(),
                ASFaceNortheast(),
                ASSetSequenceSpeed(SLOW),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
            ],
        ),
        StartAsyncEmbeddedActionScript(
            target=MARIO, prefix=0xF1, subscript=[ASSetAllSpeeds(NORMAL)]
        ),
        JmpIfBitClear(
            YOSTER_ISLE_LIBERATED_2,
            ["EVENT_3600_jmp_if_bit_set_166"],
            identifier="EVENT_3600_jmp_if_bit_clear_13",
        ),
        JmpIfBitSet(TEMP_7043_5, ["EVENT_3600_action_queue_sync_65"]),
        JmpIfBitSet(TEMP_7043_6, ["EVENT_3600_action_queue_sync_65"]),
        JmpIfBitSet(TEMP_7043_7, ["EVENT_3600_action_queue_sync_65"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=5, sprite_offset=6, is_sequence=True, looping=False
                )
            ],
        ),
        ActionQueueAsync(target=NPC_9, subscript=[ASFaceSouthwest()]),
        SetSyncActionScript(NPC_9, A0680_MUSHROOM_DERBY_UNKNOWN),
        SetSyncActionScript(MARIO, A0681_MUSHROOM_DERBY_UNKNOWN),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASWalkToXYCoords(x=17, y=49)],
            identifier="EVENT_3600_action_queue_sync_21",
        ),
        UnsyncActionScript(NPC_3),
        UnsyncActionScript(NPC_2),
        UnsyncActionScript(NPC_10),
        SetBit(TEMP_7043_1),
        SetBit(TEMP_7044_7),
        UnsyncActionScript(MARIO),
        UnsyncActionScript(NPC_9),
        PauseActionScript(MARIO),
        PauseActionScript(NPC_9),
        JmpToSubroutine(["EVENT_3600_fade_out_music_to_volume_114"]),
        JmpIfBitSet(MUSHROOM_DERBY_AUTO, ["EVENT_3600_action_queue_async_46"]),
        CopyVarToVar(from_var=UNKNOWN_70EE, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3600_play_sound_42"]),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
        SetObjectMemoryToVar(SECONDARY_TEMP_7024),
        RemoveOneOfItemFromInventory(YoshiCookie),
        EndLoop(),
        SetVarToConst(UNKNOWN_70EE, 0),
        SetVarToConst(UNKNOWN_70EB, 0),
        ActionQueueAsync(target=NPC_12, subscript=[ASSequenceLoopingOff()]),
        PlaySound(
            sound=SO063_YOSHI_TALK, channel=6, identifier="EVENT_3600_play_sound_42"
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=6,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                )
            ],
        ),
        ActionQueueAsync(target=NPC_9, subscript=[ASFaceNortheast()]),
        Jmp(["EVENT_3600_play_sound_48"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[ASResetProperties(), ASFaceNorthwest()],
            identifier="EVENT_3600_action_queue_async_46",
        ),
        PlaySound(
            sound=SO027_FOUND_AN_ITEM, channel=6, identifier="EVENT_3600_play_sound_48"
        ),
        CopyVarToVar(from_var=UNKNOWN_70D6, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
        CopyVarToVar(from_var=UNKNOWN_70BA, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
        SetVarToConst(PRIMARY_TEMP_7000, 0),
        JmpIfVarEqualsConst(
            TEMP_7026,
            0,
            ["EVENT_3600_mem_7000_shift_left_60"],
            identifier="EVENT_3600_jmp_if_var_equals_const_54",
        ),
        SetObjectMemoryToVar(SECONDARY_TEMP_7024),
        Inc(PRIMARY_TEMP_7000),
        EndLoop(),
        Dec(TEMP_7026),
        Jmp(["EVENT_3600_jmp_if_var_equals_const_54"]),
        VarShiftLeft(
            PRIMARY_TEMP_7000, 1, identifier="EVENT_3600_mem_7000_shift_left_60"
        ),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70B8),
        RunDialog(
            dialog_id=DI0943_GOT_X_COOKIES,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        RunEventAsSubroutine(E3599_MUSHROOM_DERBY_PRIZE_CALCULATOR),
        Jmp(["EVENT_3600_pause_124"]),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASWalkToXYCoords(x=17, y=49)],
            identifier="EVENT_3600_action_queue_sync_65",
        ),
        JmpToSubroutine(["EVENT_3600_jmp_if_bit_set_85"]),
        JmpIfBitSet(MUSHROOM_DERBY_AUTO, ["EVENT_3600_action_queue_async_80"]),
        PlaySound(sound=SO063_YOSHI_TALK, channel=6),
        RunDialog(
            dialog_id=DI0893_YOSHI_LOST,
            above_object=NPC_1,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        CopyVarToVar(from_var=UNKNOWN_70EE, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3600_jmp_79"]),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
        SetObjectMemoryToVar(SECONDARY_TEMP_7024),
        RemoveOneOfItemFromInventory(YoshiCookie),
        EndLoop(),
        SetVarToConst(UNKNOWN_70EE, 0),
        SetVarToConst(UNKNOWN_70EB, 0),
        ActionQueueAsync(target=NPC_12, subscript=[ASSequenceLoopingOff()]),
        Jmp(["EVENT_3600_pause_124"], identifier="EVENT_3600_jmp_79"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[ASFaceNorthwest()],
            identifier="EVENT_3600_action_queue_async_80",
        ),
        Pause(10),
        PlaySound(sound=SO063_YOSHI_TALK, channel=6),
        RunDialog(
            dialog_id=DI0894_YOSHI_LOST,
            above_object=NPC_1,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Jmp(["EVENT_3600_pause_124"]),
        JmpIfBitSet(
            TEMP_7043_7,
            ["EVENT_3600_unsync_action_script_92"],
            identifier="EVENT_3600_jmp_if_bit_set_85",
        ),
        JmpIfBitSet(TEMP_7043_6, ["EVENT_3600_unsync_action_script_98"]),
        JmpIfBitSet(TEMP_7043_5, ["EVENT_3600_unsync_action_script_104"]),
        UnsyncActionScript(NPC_3),
        UnsyncActionScript(NPC_2),
        UnsyncActionScript(NPC_10),
        Jmp(["EVENT_3600_pause_action_script_109"]),
        UnsyncActionScript(NPC_2, identifier="EVENT_3600_unsync_action_script_92"),
        UnsyncActionScript(NPC_10),
        SetBit(TEMP_7044_7),
        PauseActionScript(NPC_3),
        UnsyncActionScript(NPC_3),
        Jmp(["EVENT_3600_pause_action_script_109"]),
        UnsyncActionScript(NPC_3, identifier="EVENT_3600_unsync_action_script_98"),
        UnsyncActionScript(NPC_10),
        SetBit(TEMP_7044_7),
        PauseActionScript(NPC_2),
        UnsyncActionScript(NPC_2),
        Jmp(["EVENT_3600_pause_action_script_109"]),
        UnsyncActionScript(NPC_3, identifier="EVENT_3600_unsync_action_script_104"),
        UnsyncActionScript(NPC_2),
        SetBit(TEMP_7044_7),
        PauseActionScript(NPC_10),
        UnsyncActionScript(NPC_10),
        PauseActionScript(NPC_2, identifier="EVENT_3600_pause_action_script_109"),
        PauseActionScript(NPC_3),
        PauseActionScript(NPC_10),
        PauseActionScript(NPC_5),
        PauseActionScript(NPC_0),
        FadeOutMusicToVolume(
            duration=3, volume=0, identifier="EVENT_3600_fade_out_music_to_volume_114"
        ),
        Pause(120),
        PlayMusicAtDefaultVolume(M04_YOSTER_ISLAND),
        JmpIfBitSet(MUSHROOM_DERBY_AUTO, ["EVENT_3600_action_queue_async_121"]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASShiftNortheastPixels(8),
                ASShiftNortheastSteps(2),
                ASShiftSoutheastSteps(2),
                ASSetSequenceSpeed(SLOW),
                ASFaceSouthwest(),
            ],
        ),
        Pause(30),
        Return(),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASShiftNortheastPixels(8),
                ASShiftNortheastSteps(2),
                ASShiftSoutheastSteps(1),
                ASSetSequenceSpeed(SLOW),
            ],
            identifier="EVENT_3600_action_queue_async_121",
        ),
        Pause(30),
        Return(),
        Pause(30, identifier="EVENT_3600_pause_124"),
        SetVarToConst(ROSE_TOWN_ARROW_POSITION, 0),
        ClearBit(TEMP_7043_0),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7043_2),
        ClearBit(TEMP_7043_4),
        ClearBit(TEMP_7043_5),
        ClearBit(TEMP_7043_6),
        ClearBit(TEMP_7043_7),
        ClearBit(TEMP_7044_6),
        ClearBit(TEMP_7044_7),
        SetBit(TEMP_7043_3),
        ClearBit(TEMP_7044_0),
        ClearBit(TEMP_7044_1),
        ClearBit(TEMP_7044_2),
        ClearBit(TEMP_7044_3),
        ClearBit(TEMP_7044_6),
        JmpToSubroutine(["EVENT_3600_action_queue_sync_329"]),
        SetSyncActionScript(NPC_2, A0682_MUSHROOM_DERBY_UNKNOWN),
        SetSyncActionScript(NPC_10, A0685_MUSHROOM_DERBY_UNKNOWN),
        SetSyncActionScript(NPC_3, A0683_MUSHROOM_DERBY_UNKNOWN),
        SetSyncActionScript(NPC_5, A0098_WALK_RANDOM_DIRECTIONS_NO_SOLIDITY_CHANGE),
        ActionQueueAsync(target=NPC_0, subscript=[ASFaceNorthwest()]),
        SetSyncActionScript(NPC_0, A0677_MUSHROOM_DERBY_UNKNOWN),
        SetBit(TEMP_7044_5),
        SetBit(TEMP_7044_4),
        SetVarToConst(ROSE_WAY_703E, 7),
        UnfreezeCamera(),
        JmpIfBitSet(MUSHROOM_DERBY_AUTO, ["EVENT_3600_enable_controls_158"]),
        RunBackgroundEvent(
            event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, bit_7=True
        ),
        EnableControls([LEFT, RIGHT, DOWN, UP]),
        SetSyncActionScript(NPC_1, A0684_MUSHROOM_DERBY_UNKNOWN),
        ClearBit(MUSHROOM_DERBY_MANUAL),
        Return(),
        EnableControls(
            [LEFT, RIGHT, DOWN, UP, X, A, Y, B],
            identifier="EVENT_3600_enable_controls_158",
        ),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
                ASSetSolidityBits(cant_walk_through=True),
                ASSetSolidityBits(bit_4=True),
                ASSetSolidityBits(cant_pass_walls=True),
            ],
        ),
        SetSyncActionScript(NPC_1, A0496_MUSHROOM_DERBY_REFEREE),
        ClearBit(MUSHROOM_DERBY_AUTO),
        ClearBit(TEMP_7044_5),
        ClearBit(TEMP_7044_4),
        Return(),
        JmpIfBitSet(
            TEMP_7043_5,
            ["EVENT_3600_set_bit_288"],
            identifier="EVENT_3600_jmp_if_bit_set_166",
        ),
        SetVarToConst(UNKNOWN_70EE, 0),
        SetVarToConst(UNKNOWN_70EB, 0),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=5, sprite_offset=6, is_sequence=True, looping=False
                )
            ],
        ),
        ActionQueueAsync(target=NPC_9, subscript=[ASFaceSouthwest()]),
        SetSyncActionScript(NPC_9, A0680_MUSHROOM_DERBY_UNKNOWN),
        SetSyncActionScript(MARIO, A0681_MUSHROOM_DERBY_UNKNOWN),
        SetBit(TEMP_7049_2),
        RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
        UnsyncActionScript(NPC_10),
        ActionQueueAsync(
            target=NPC_10,
            subscript=[ASBounceToXYWithHeight(x=21, y=63, height=0), ASFaceNorthwest()],
        ),
        PauseActionScript(NPC_0),
        PauseActionScript(NPC_2),
        PauseActionScript(NPC_1),
        PauseActionScript(NPC_3),
        SetBit(TEMP_7043_1),
        UnsyncActionScript(MARIO),
        UnsyncActionScript(NPC_9),
        PauseActionScript(MARIO),
        PauseActionScript(NPC_9),
        Pause(10),
        FadeOutMusicToVolume(duration=3, volume=0),
        Pause(120),
        StopMusic(),
        PlayMusicAtDefaultVolume(M04_YOSTER_ISLAND),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASShiftNortheastSteps(2),
                ASShiftSoutheastSteps(2),
                ASFaceSouthwest(),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
                ASSetSequenceSpeed(SLOW),
                ASSequenceLoopingOn(),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetAllSpeeds(VERY_FAST),
                ASShiftNorthwestSteps(6),
                ASShiftNortheastSteps(12),
                ASFaceSoutheast(),
                ASSetSequenceSpeed(SLOW),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASShiftNorthwestSteps(4),
                ASShiftNortheastSteps(2),
                ASSetSequenceSpeed(SLOW),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
            ],
        ),
        RememberLastObject(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=6,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                )
            ],
        ),
        ActionQueueAsync(target=NPC_9, subscript=[ASFaceNortheast()]),
        SetAsyncActionScript(NPC_5, A0636_54_VELOCITY_SINGLE_JUMP),
        SetAsyncActionScript(NPC_0, A0636_54_VELOCITY_SINGLE_JUMP),
        Pause(10),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=6, sprite_offset=6, is_sequence=True, looping=True
                )
            ],
        ),
        ActionQueueAsync(target=NPC_9, subscript=[ASFaceNorthwest()]),
        Pause(10),
        Pause(10),
        SetAsyncActionScript(NPC_10, A0636_54_VELOCITY_SINGLE_JUMP),
        Pause(10),
        StartSyncEmbeddedActionScript(
            target=NPC_9, prefix=0xF1, subscript=[ASFaceSoutheast()]
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=5,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=False,
                    mirror_sprite=True,
                )
            ],
        ),
        Pause(10),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASSetSpriteSequence(
                    index=20,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(10),
                ASResetProperties(),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=6,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                )
            ],
        ),
        ActionQueueAsync(target=NPC_9, subscript=[ASFaceNortheast()]),
        SetAsyncActionScript(NPC_5, A0636_54_VELOCITY_SINGLE_JUMP),
        Pause(10),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=6, sprite_offset=6, is_sequence=True, looping=True
                )
            ],
        ),
        ActionQueueAsync(target=NPC_9, subscript=[ASFaceNorthwest()]),
        Pause(10),
        SetAsyncActionScript(NPC_0, A0636_54_VELOCITY_SINGLE_JUMP),
        Pause(10),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=5, sprite_offset=6, is_sequence=True, looping=True
                )
            ],
        ),
        ActionQueueAsync(target=NPC_9, subscript=[ASFaceSouthwest()]),
        Pause(10),
        SetAsyncActionScript(NPC_1, A0636_54_VELOCITY_SINGLE_JUMP),
        Pause(10),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=5,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                )
            ],
        ),
        ActionQueueAsync(target=NPC_9, subscript=[ASFaceSoutheast()]),
        Pause(10),
        ActionQueueSync(
            target=MARIO, subscript=[ASJumpToHeight(height=64, silent=True)]
        ),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASPause(3),
                ASSetSpriteSequence(
                    index=21,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(5),
                ASResetProperties(),
                ASPause(
                    1, identifier="EVENT_3600_action_queue_async_240_SUBSCRIPT_pause_4"
                ),
                ASJmpIfObjectInAir(
                    NPC_9, ["EVENT_3600_action_queue_async_240_SUBSCRIPT_pause_4"]
                ),
            ],
        ),
        Pause(10),
        SetBit(COMPLETED_MUSHROOM_DERBY),
        PlaySound(sound=SO063_YOSHI_TALK, channel=6),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(height=108, silent=True),
                ASPause(
                    1, identifier="EVENT_3600_action_queue_sync_250_SUBSCRIPT_pause_1"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3600_action_queue_sync_250_SUBSCRIPT_pause_1"]
                ),
            ],
        ),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASPause(8),
                ASSetSpriteSequence(
                    index=21,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(8),
                ASResetProperties(),
            ],
        ),
        CircleMaskShrinkToObject(target=MARIO, width=0, speed=3, static=True),
        PauseScriptUntilEffectDone(),
        SetBit(YOSTER_ISLE_LIBERATED_1),
        EnterArea(
            room_id=R034_YOSTER_ISLE,
            face_direction=NORTHWEST,
            x=20,
            y=61,
            z=0,
            run_entrance_event=True,
        ),
        PauseActionScript(NPC_3),
        PauseActionScript(NPC_9),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASResetProperties(),
                ASTransferToXYZF(x=21, y=62, z=0, direction=EAST),
            ],
        ),
        StartAsyncEmbeddedActionScript(
            target=NPC_9,
            prefix=0xF1,
            subscript=[
                ASTransferToXYZF(x=20, y=61, z=0, direction=EAST),
                ASFaceSoutheast(),
            ],
        ),
        FadeInFromBlack(sync=True, duration=120),
        PauseScriptUntilEffectDone(),
        Pause(60),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        Pause(10),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        Pause(10),
        RunEventAsSubroutine(E0180_NPC_QUEST_3_CONTAINER),
        Pause(10),
        RunEventAsSubroutine(E0181_NPC_QUEST_4_CONTAINER),
        Pause(10),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        Pause(30),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASPlaySound(sound=SO063_YOSHI_TALK, channel=6),
                ASSetSpriteSequence(
                    index=21,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(10),
                ASResetProperties(),
                ASPause(30),
            ],
        ),
        SetSyncActionScript(NPC_3, A0676_MUSHROOM_DERBY_UNKNOWN),
        ActionQueueSync(
            target=MARIO,
            subscript=[ASPause(30), ASFaceNorth(), ASPause(60), ASFaceSouth()],
        ),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASSetSequenceSpeed(FAST),
                ASShiftNortheastSteps(2),
                ASSetSequenceSpeed(NORMAL),
            ],
        ),
        SetSyncActionScript(NPC_9, A0021_STAND_STILL_AND_MOVE_RANDOM_DIRECTIONS),
        SetBit(YOSTER_ISLE_LIBERATED_2),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        Return(),
        SetBit(TEMP_7043_1, identifier="EVENT_3600_set_bit_288"),
        PauseActionScript(NPC_10),
        UnsyncActionScript(NPC_10),
        PauseActionScript(NPC_0),
        PauseActionScript(NPC_2),
        PauseActionScript(NPC_1),
        PauseActionScript(NPC_3),
        PauseActionScript(NPC_10),
        Pause(30),
        FadeOutMusicToVolume(duration=3, volume=0),
        Pause(120),
        StopMusic(),
        PlayMusicAtDefaultVolume(M04_YOSTER_ISLAND),
        ActionQueueAsync(target=NPC_10, subscript=[ASFaceNorthwest()]),
        Pause(30),
        StartSyncEmbeddedActionScript(
            target=NPC_9, prefix=0xF1, subscript=[ASFaceSoutheast()]
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=5,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=False,
                    mirror_sprite=True,
                )
            ],
        ),
        PlaySound(sound=SO062_BIG_YOSHI_TALK, channel=6),
        CircleMaskShrinkToObject(target=MARIO, width=0, speed=3, static=True),
        PauseScriptUntilEffectDone(),
        SetBit(YOSTER_ISLE_LIBERATED_1),
        EnterArea(
            room_id=R034_YOSTER_ISLE,
            face_direction=NORTHWEST,
            x=20,
            y=61,
            z=0,
            run_entrance_event=True,
        ),
        PauseActionScript(NPC_3),
        PauseActionScript(NPC_9),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASResetProperties(),
                ASTransferToXYZF(x=21, y=62, z=0, direction=EAST),
            ],
        ),
        StartAsyncEmbeddedActionScript(
            target=NPC_9,
            prefix=0xF1,
            subscript=[
                ASTransferToXYZF(x=20, y=61, z=0, direction=EAST),
                ASFaceSoutheast(),
            ],
        ),
        FadeInFromBlack(sync=True, duration=120),
        PauseScriptUntilEffectDone(),
        Pause(60),
        PlaySound(sound=SO063_YOSHI_TALK, channel=6),
        Pause(10),
        SetAsyncActionScript(MARIO, A0670_NOD_YES),
        Pause(10),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASSetSpriteSequence(
                    index=21,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASPause(10),
                ASResetProperties(),
                ASPause(30),
            ],
        ),
        SetSyncActionScript(NPC_3, A0676_MUSHROOM_DERBY_UNKNOWN),
        SetSyncActionScript(NPC_9, A0119_SLOW_SEQUENCE_LOOP),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        ClearBit(GOT_FREE_COOKIES),
        Return(),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
            ],
            identifier="EVENT_3600_action_queue_sync_329",
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
            ],
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
            ],
        ),
        StartSyncEmbeddedActionScript(
            target=NPC_5,
            prefix=0xF1,
            subscript=[
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetSolidityBits(cant_pass_walls=True),
                ASSetObjectMemoryBits(arg_1=0x0B, bits=[1]),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
            ],
        ),
        ActionQueueSync(
            target=NPC_10,
            subscript=[
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                )
            ],
        ),
        Return(),
    ]
)
