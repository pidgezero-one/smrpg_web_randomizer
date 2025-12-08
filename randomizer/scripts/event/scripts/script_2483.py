# pylint: disable=C0301

"""E2483_BEAN_VALLEY_LEFTMOST_PIRANHA"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfRandom1of2(["EVENT_2483_start_battle_3"]),
        StartBattleAtBattlefield(88, BF41_BEAN_VALLEY_GRASSLANDS),
        Jmp(["EVENT_2483_jmp_if_bit_set_4"]),
        StartBattleAtBattlefield(
            89, BF41_BEAN_VALLEY_GRASSLANDS, identifier="EVENT_2483_start_battle_3"
        ),
        JmpIfBitSet(
            RUN_AWAY,
            ["EVENT_2483_set_temp_action_script_sync_12"],
            identifier="EVENT_2483_jmp_if_bit_set_4"),
        JmpIfBitSet(GAME_OVER, ["EVENT_2483_reset_and_choose_game_15"]),
        RemoveObjectFromSpecificLevel(NPC_5, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        RemoveObjectFromSpecificLevel(NPC_11, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        RemoveObjectFromCurrentLevel(NPC_5),
        RemoveObjectFromCurrentLevel(NPC_11),
        FadeInFromBlack(sync=False),
        Return(),
        SetTempSyncActionScript(
            NPC_11,
            A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES,
            identifier="EVENT_2483_set_temp_action_script_sync_12"),
        FadeInFromBlack(sync=False),
        Return(),
        ResetAndChooseGame(identifier="EVENT_2483_reset_and_choose_game_15"),
        Return(),
    ]
)
