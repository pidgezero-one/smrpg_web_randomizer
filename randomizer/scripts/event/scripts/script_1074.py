# pylint: disable=C0301

"""E1074_MELODY_BAY_SONG_JUDGED"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_7044_2, identifier="EVENT_1074_set_bit_0"),
        UnfreezeCamera(),
        StopMusicFDA2(),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFaceNortheast(),
                ASSetSpriteSequence(
                    index=2,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASWalkNortheastPixels(8),
                ASPause(45),
                ASSetPriority(2),
                ASResetProperties(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(NORMAL),
                ASSetSolidityBits(cant_pass_walls=True),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFaceSouthwest(),
                ASSetSpriteSequence(
                    index=3, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASSequenceLoopingOn(),
                ASReturn(),
            ],
        ),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASPause(30),
                ASSetWalkingSpeed(SLOW),
                ASWalkSouthwestPixels(4),
                ASSetWalkingSpeed(NORMAL),
                ASWalkSouthwestPixels(8),
                ASSetWalkingSpeed(FAST),
                ASWalkSouthwestSteps(9),
                ASSetWalkingSpeed(NORMAL),
                ASWalkSouthwestPixels(8),
                ASSetWalkingSpeed(SLOW),
                ASWalkSouthwestPixels(4),
            ],
        ),
        Pause(15),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(SLOW), ASWalkNortheastSteps(12)],
        ),
        JmpIfBitSet(TOADOFSKY_REMOVED, ["EVENT_1074_set_7000_to_7000_short_mem_7"]),
        JmpIfBitSet(
            MELODY_BAY_ITEM_3_GRANTED, ["EVENT_1074_set_7000_to_7000_short_mem_7"]
        ),
        JmpIfBitSet(
            MELODY_BAY_ITEM_2_GRANTED, ["EVENT_1074_third_song_not_unlocked_yet"]
        ),
        JmpIfBitSet(
            MELODY_BAY_ITEM_1_GRANTED, ["EVENT_1074_second_song_not_unlocked_yet"]
        ),
        JmpToEvent(E1079_MELODY_BAY_SONG_1_VALIDATOR),
        JmpIfBitClear(
            MINECART_CLEARED,
            ["EVENT_1074_set_7000_to_7000_short_mem_7"],
            identifier="EVENT_1074_second_song_not_unlocked_yet",
        ),
        JmpToEvent(E1080_MELODY_BAY_SONG_2_VALIDATOR),
        JmpIfBitClear(
            MELODY_BAY_SONG_3_UNLOCKED,
            ["EVENT_1074_set_7000_to_7000_short_mem_7"],
            identifier="EVENT_1074_third_song_not_unlocked_yet",
        ),
        JmpToEvent(E1081_MELODY_BAY_SONG_3_VALIDATOR),
        CopyVarToVar(
            from_var=SECONDARY_TEMP_7024,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_1074_set_7000_to_7000_short_mem_7",
        ),
        JmpToSubroutine(["EVENT_1074_jmp_if_7000_equals_short_369"]),
        SetSyncActionScript(NPC_0, A0572_MELODY_BAY_TADPOLE_INCORRECT),
        ClearBit(TEMP_7043_0),
        Pause(35),
        CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
        JmpToSubroutine(["EVENT_1074_jmp_if_7000_equals_short_369"]),
        SetSyncActionScript(NPC_1, A0572_MELODY_BAY_TADPOLE_INCORRECT),
        ClearBit(TEMP_7043_1),
        Pause(35),
        CopyVarToVar(from_var=TEMP_7028, to_var=PRIMARY_TEMP_7000),
        JmpToSubroutine(["EVENT_1074_jmp_if_7000_equals_short_369"]),
        SetSyncActionScript(NPC_2, A0572_MELODY_BAY_TADPOLE_INCORRECT),
        ClearBit(TEMP_7043_2),
        Pause(35),
        CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
        JmpToSubroutine(["EVENT_1074_jmp_if_7000_equals_short_369"]),
        SetSyncActionScript(NPC_3, A0572_MELODY_BAY_TADPOLE_INCORRECT),
        ClearBit(TEMP_7043_3),
        Pause(35),
        CopyVarToVar(from_var=TEMP_702C, to_var=PRIMARY_TEMP_7000),
        JmpToSubroutine(["EVENT_1074_jmp_if_7000_equals_short_369"]),
        SetSyncActionScript(NPC_4, A0572_MELODY_BAY_TADPOLE_INCORRECT),
        ClearBit(TEMP_7043_4),
        Pause(35),
        CopyVarToVar(from_var=TEMP_702E, to_var=PRIMARY_TEMP_7000),
        JmpToSubroutine(["EVENT_1074_jmp_if_7000_equals_short_369"]),
        SetSyncActionScript(NPC_5, A0572_MELODY_BAY_TADPOLE_INCORRECT),
        ClearBit(TEMP_7043_5),
        Pause(35),
        CopyVarToVar(from_var=TEMP_7030, to_var=PRIMARY_TEMP_7000),
        JmpToSubroutine(["EVENT_1074_jmp_if_7000_equals_short_369"]),
        SetSyncActionScript(NPC_6, A0572_MELODY_BAY_TADPOLE_INCORRECT),
        ClearBit(TEMP_7043_6),
        Pause(35),
        CopyVarToVar(from_var=TEMP_7032, to_var=PRIMARY_TEMP_7000),
        JmpToSubroutine(["EVENT_1074_jmp_if_7000_equals_short_369"]),
        SetSyncActionScript(NPC_7, A0572_MELODY_BAY_TADPOLE_INCORRECT),
        ClearBit(TEMP_7043_7),
        Pause(35),
        Pause(45),
        PlayMusicAtCurrentVolume(M17_TADPOLE_POND),
        Jmp(["EVENT_1074_action_queue_async_190"]),
        Pause(15, identifier="EVENT_1074_pause_107"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(5),
                ASResetProperties(),
                ASSequenceLoopingOff(),
                ASFaceNorthwest(),
                ASPause(5),
            ],
        ),
        RunDialog(
            dialog_id=DI2725_SONG_SIMILARITY_0,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
        Pause(15, identifier="EVENT_1074_pause_113"),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(15),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(5),
                ASResetProperties(),
                ASSequenceLoopingOff(),
                ASFaceNorthwest(),
                ASPause(5),
            ],
        ),
        RunDialog(
            dialog_id=DI2726_SONG_SIMILARITY_1,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[ASSetSpriteSequence(index=0, is_sequence=True, looping=True)],
        ),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
        Pause(15, identifier="EVENT_1074_pause_121"),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(15),
                ASSetAllSpeeds(NORMAL),
                ASSetSpriteSequence(
                    index=1, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASWalkSoutheastSteps(2),
                ASSetSpriteSequence(
                    index=1, is_mold=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(5),
                ASResetProperties(),
                ASSequenceLoopingOff(),
                ASFaceNorthwest(),
                ASPause(5),
            ],
        ),
        RunDialog(
            dialog_id=DI2727_SONG_SIMILARITY_2,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetSequenceSpeed(SLOW),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ],
        ),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
        Pause(15, identifier="EVENT_1074_pause_129"),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASPause(15),
                ASSetAllSpeeds(FAST),
                ASSetSpriteSequence(
                    index=1, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASWalkSoutheastSteps(2),
                ASWalkSoutheastPixels(8),
                ASSetSpriteSequence(
                    index=1, is_mold=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(5),
                ASResetProperties(),
                ASSequenceLoopingOff(),
                ASFaceNorthwest(),
                ASPause(5),
            ],
        ),
        RunDialog(
            dialog_id=DI2728_SONG_SIMILARITY_3,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ],
        ),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
        Pause(15, identifier="EVENT_1074_pause_137"),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_mold=True, looping=True, mirror_sprite=True
                ),
                ASSetAllSpeeds(VERY_FAST),
                ASSetSpriteSequence(
                    index=1, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASWalkSoutheastSteps(2),
                ASWalkSoutheastPixels(10),
                ASSetSpriteSequence(
                    index=1, is_mold=True, looping=True, mirror_sprite=True
                ),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(5),
                ASResetProperties(),
                ASSequenceLoopingOff(),
                ASFaceNorthwest(),
                ASPause(5),
            ],
        ),
        RunDialog(
            dialog_id=DI2729_SONG_SIMILARITY_4,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ],
        ),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
        Pause(15, identifier="EVENT_1074_pause_145"),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASJumpToHeight(96),
                ASPause(60),
                ASSetSpriteSequence(
                    index=1, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASSetAllSpeeds(VERY_FAST),
                ASWalkSoutheastSteps(2),
                ASWalkSoutheastPixels(8),
            ],
        ),
        Pause(15),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASResetProperties(),
                ASSequenceLoopingOff(),
                ASFaceNorthwest(),
                ASSetPriority(2),
            ],
        ),
        Pause(15),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
            ],
        ),
        Pause(15),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetSpriteSequence(
                    index=2, is_sequence=True, looping=True, mirror_sprite=True
                )
            ],
        ),
        JmpIfBitClear(MELODY_BAY_ITEM_1_GRANTED, ["EVENT_1074_set_157"]),
        JmpIfBitClear(MELODY_BAY_ITEM_2_GRANTED, ["EVENT_1074_set_162"]),
        JmpIfBitClear(MELODY_BAY_ITEM_3_GRANTED, ["EVENT_1074_set_168"]),
        RunEventAsSubroutine(
            E0178_NPC_QUEST_1_CONTAINER, identifier="EVENT_1074_set_157"
        ),
        Pause(30),
        SetBit(MELODY_BAY_ITEM_1_GRANTED),
        Jmp(["EVENT_1074_action_queue_async_185"]),
        RunEventAsSubroutine(
            E0179_NPC_QUEST_2_CONTAINER, identifier="EVENT_1074_set_162"
        ),
        Pause(30),
        SetBit(MELODY_BAY_ITEM_2_GRANTED),
        Jmp(["EVENT_1074_action_queue_async_185"]),
        RunEventAsSubroutine(
            E0180_NPC_QUEST_3_CONTAINER, identifier="EVENT_1074_set_168"
        ),
        Pause(30),
        SetBit(MELODY_BAY_ITEM_3_GRANTED),
        SetBit(UNKNOWN_7093_0),
        ActionQueueAsync(
            target=NPC_8,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASSetSequenceSpeed(VERY_FAST),
                ASSetWalkingSpeed(FAST),
                ASJumpToHeight(112),
                ASWalkSoutheastSteps(7),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
                ASPause(80),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASWalkSouthwestSteps(8),
                ASVisibilityOff(),
            ],
            identifier="EVENT_1074_action_queue_async_185",
        ),
        RemoveObjectFromCurrentLevel(NPC_8),
        SetBit(TOADOFSKY_REMOVED),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(5),
                ASResetProperties(),
                ASSequenceLoopingOff(),
                ASFaceSouthwest(),
                ASPause(5),
            ],
            identifier="EVENT_1074_action_queue_async_190",
        ),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000,
            0,
            ["EVENT_1074_play_sound_376"],
            identifier="EVENT_1074_jmp_if_7000_equals_short_369",
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1074_play_sound_378"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_1074_play_sound_380"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_1074_play_sound_382"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_1074_play_sound_384"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_1074_play_sound_386"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_1074_play_sound_388"]),
        PlaySound(
            sound=SO036_TADPOLE_POND_STAFF_DO,
            channel=6,
            identifier="EVENT_1074_play_sound_376",
        ),
        Return(),
        PlaySound(
            sound=SO037_TADPOLE_POND_STAFF_RE,
            channel=6,
            identifier="EVENT_1074_play_sound_378",
        ),
        Return(),
        PlaySound(
            sound=SO038_TADPOLE_POND_STAFF_MI,
            channel=6,
            identifier="EVENT_1074_play_sound_380",
        ),
        Return(),
        PlaySound(
            sound=SO039_TADPOLE_POND_STAFF_FA,
            channel=6,
            identifier="EVENT_1074_play_sound_382",
        ),
        Return(),
        PlaySound(
            sound=SO040_TADPOLE_POND_STAFF_SO,
            channel=6,
            identifier="EVENT_1074_play_sound_384",
        ),
        Return(),
        PlaySound(
            sound=SO041_TADPOLE_POND_STAFF_LA,
            channel=6,
            identifier="EVENT_1074_play_sound_386",
        ),
        Return(),
        PlaySound(
            sound=SO042_TADPOLE_POND_STAFF_TI,
            channel=6,
            identifier="EVENT_1074_play_sound_388",
        ),
        Return(),
    ]
)
