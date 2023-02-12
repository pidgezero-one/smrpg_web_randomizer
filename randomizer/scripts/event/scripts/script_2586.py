# E2586_BOOSTER_PASS_APPRENTICE_FIGHT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(target=NPC_9, subscript=[ASSetPriority(3)]),
        RunEventAsSubroutine(E1186_HENCHMAN_BATTLE_PACK_SELECTOR),
        JmpIfBitSet(RUN_AWAY, ["EVENT_2586_set_temp_action_script_sync_14"]),
        JmpIfBitSet(GAME_OVER, ["EVENT_2586_stop_music_FD9F_17"]),
        FadeInFromBlack(sync=False),
        SetAsyncActionScript(NPC_9, A0851_BOOSTER_PASS_APPRENTICE_AFTER_FIGHT),
        Return(),
        SetTempSyncActionScript(
            NPC_9,
            A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES,
            identifier="EVENT_2586_set_temp_action_script_sync_14",
        ),
        FadeInFromBlack(sync=False),
        Return(),
        StopMusicFD9F(identifier="EVENT_2586_stop_music_FD9F_17"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=8, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASFaceSouthwest(),
            ],
        ),
        FadeInFromBlack(sync=False),
        SetAsyncActionScript(NPC_9, A0851_BOOSTER_PASS_APPRENTICE_AFTER_FIGHT),
        Pause(16),
        SetAsyncActionScript(MARIO, A0384_PLAYER_LOOK_DOWN_SHAKE_HEAD),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
    ]
)
