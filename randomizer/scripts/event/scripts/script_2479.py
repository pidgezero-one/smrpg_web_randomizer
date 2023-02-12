# E2479_BEAN_VALLEY_BOTTOM_LEFT_PIRANHA

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfRandom1of2(["EVENT_2479_start_battle_3"]),
        StartBattleAtBattlefield(88, BF41_BEAN_VALLEY_GRASSLANDS),
        Jmp(["EVENT_2479_jmp_if_bit_set_4"]),
        StartBattleAtBattlefield(
            89, BF41_BEAN_VALLEY_GRASSLANDS, identifier="EVENT_2479_start_battle_3"
        ),
        JmpIfBitSet(
            RUN_AWAY,
            ["EVENT_2479_set_temp_action_script_sync_12"],
            identifier="EVENT_2479_jmp_if_bit_set_4",
        ),
        JmpIfBitSet(GAME_OVER, ["EVENT_2479_reset_and_choose_game_15"]),
        RemoveObjectFromSpecificLevel(NPC_0, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        RemoveObjectFromSpecificLevel(NPC_6, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromCurrentLevel(NPC_6),
        FadeInFromBlack(sync=False),
        Return(),
        SetTempSyncActionScript(
            NPC_6,
            A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES,
            identifier="EVENT_2479_set_temp_action_script_sync_12",
        ),
        FadeInFromBlack(sync=False),
        Return(),
        ResetAndChooseGame(identifier="EVENT_2479_reset_and_choose_game_15"),
        Return(),
    ]
)
