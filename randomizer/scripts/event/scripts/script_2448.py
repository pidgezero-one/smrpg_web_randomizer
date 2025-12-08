# pylint: disable=C0301

"""E2448_FOREST_BOSS_FIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(FOREST_LIBERATED, ["EVENT_2448_ret_272"]),
        ClearBit(DIRECTIONAL_7045_0),
        ClearBit(DIRECTIONAL_7045_1),
        ClearBit(DIRECTIONAL_7045_2),
        ClearBit(DIRECTIONAL_7045_3),
        ClearBit(DIRECTIONAL_7045_4),
        ClearBit(DIRECTIONAL_7045_5),
        ClearBit(DIRECTIONAL_7045_6),
        ClearBit(DIRECTIONAL_7045_7),
        ClearBit(DIRECTIONAL_7046_0),
        ClearBit(DIRECTIONAL_7046_1),
        ActionQueueSync(target=NPC_11, subscript=[ASSetPriority(3)]),
        ActionQueueAsync(target=MARIO, subscript=[ASWalkNorthwestSteps(2)]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(30),
                ASSetSpriteSequence(
                    index=3,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
            ]),
        ActionQueueAsync(target=SCREEN_FOCUS, subscript=[ASWalkNorthwestSteps(10)]),
        JmpIfObjectNotInSpecificLevel(
            NPC_1, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD, ["EVENT_2448_pause_42"]
        ),
        SetSyncActionScript(NPC_0, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
        SetSyncActionScript(NPC_5, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
        SetSyncActionScript(NPC_1, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
        SetSyncActionScript(NPC_6, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
        SetSyncActionScript(NPC_2, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
        SetSyncActionScript(NPC_7, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
        SetSyncActionScript(NPC_3, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
        SetSyncActionScript(NPC_8, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
        SetSyncActionScript(NPC_4, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
        SetSyncActionScript(NPC_9, A0487_FOREST_BOSS_ROOM_HENCHMEN_JUMP),
        RunBackgroundEvent(
            event_id=E2446_FOREST_BOSS_HENCHMEN_BOUNCE, return_on_level_exit=True
        ),
        ActionQueueSync(
            target=NPC_11, subscript=[ASSetPriority(3), ASSetSequenceSpeed(FASTER)]
        ),
        Pause(180, identifier="EVENT_2448_pause_42"),
        SetBit(TEMP_7043_0),
        StopAllBackgroundEvents(),
        Pause(16),
        PlaySound(sound=SO019_LONG_FALL, channel=6),
        ActionQueueSync(
            target=NPC_11,
            subscript=[ASFaceSoutheast(), ASPause(16), ASSequenceLoopingOff()]),
        Pause(112),
        ActionQueueAsync(
            target=NPC_10,
            subscript=[
                ASTransferToXYZF(x=10, y=29, z=0, direction=SOUTHEAST),
                ASVisibilityOn(),
                ASSequencePlaybackOff(),
                ASFloatingOn(),
                ASJumpToHeight(height=1, silent=True),
                ASSetSpriteSequence(
                    index=20, is_mold=True, is_sequence=True, looping=True
                ),
                ASPause(
                    1, identifier="EVENT_2448_action_queue_async_84_SUBSCRIPT_pause_6"
                ),
                ASJmpIfObjectInAir(
                    NPC_10, ["EVENT_2448_action_queue_async_84_SUBSCRIPT_pause_6"]
                ),
                ASPlaySound(sound=SO058_INSERT, channel=6),
                ASPause(8),
                ASSequencePlaybackOn(),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASPause(16),
                ASSetSpriteSequence(
                    index=17,
                    sprite_offset=1,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
            ]),
        ActionQueueSync(
            target=NPC_10,
            subscript=[
                ASPause(16),
                ASSetSpriteSequence(
                    index=17,
                    sprite_offset=1,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
            ]),
        ActionQueueSync(
            target=NPC_11, subscript=[ASSetSequenceSpeed(FASTER), ASSequenceLoopingOn()]
        ),
        RunEventAsSubroutine(E0186_PARTY_JOIN_LOGIC),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        RunEventAsSubroutine(E0211_UNLOCK_PIPE_VAULT_IF_GATED_BY_FOREST_MAZE),
        JmpIfBitClear(GAME_OVER, ["EVENT_2448_set_bit_94"]),
        ResetAndChooseGame(),
        SetBit(FOREST_LIBERATED, identifier="EVENT_2448_set_bit_94"),
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromCurrentLevel(NPC_3),
        RemoveObjectFromCurrentLevel(NPC_4),
        RemoveObjectFromCurrentLevel(NPC_5),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromCurrentLevel(NPC_7),
        RemoveObjectFromCurrentLevel(NPC_8),
        RemoveObjectFromCurrentLevel(NPC_9),
        RemoveObjectFromCurrentLevel(NPC_10),
        RemoveObjectFromCurrentLevel(NPC_11),
        RemoveObjectFromSpecificLevel(NPC_0, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
        RemoveObjectFromSpecificLevel(NPC_1, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
        RemoveObjectFromSpecificLevel(NPC_2, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
        RemoveObjectFromSpecificLevel(NPC_3, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
        RemoveObjectFromSpecificLevel(NPC_4, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
        RemoveObjectFromSpecificLevel(NPC_5, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
        RemoveObjectFromSpecificLevel(NPC_6, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
        RemoveObjectFromSpecificLevel(NPC_7, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
        RemoveObjectFromSpecificLevel(NPC_8, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
        RemoveObjectFromSpecificLevel(NPC_9, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
        RemoveObjectFromSpecificLevel(NPC_10, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
        RemoveObjectFromSpecificLevel(NPC_11, R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD),
        RemoveObjectFromSpecificLevel(NPC_11, R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09),
        RemoveObjectFromSpecificLevel(NPC_1, R228_FOREST_MAZE_AREA_04),
        ActionQueueAsync(
            target=MARIO, subscript=[ASResetProperties(), ASTransferToObjectXYZ(NPC_10)]
        ),
        FadeInFromBlack(sync=False),
        RestoreAllHP(),
        RestoreAllFP(),
        PlayMusicAtDefaultVolume(M26_FOREST_MAZE),
        UnfreezeCamera(),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(identifier="EVENT_2448_ret_272"),
    ]
)
