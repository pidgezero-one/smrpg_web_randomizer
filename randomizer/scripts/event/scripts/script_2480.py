# pylint: disable=C0301

"""E2480_BEAN_VALLEY_BOTTOM_RIGHT_PIRANHA"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfRandom1of2(["EVENT_2480_start_battle_3"]),
        StartBattleAtBattlefield(88, BF41_BEAN_VALLEY_GRASSLANDS),
        Jmp(["EVENT_2480_jmp_if_bit_set_4"]),
        StartBattleAtBattlefield(
            89, BF41_BEAN_VALLEY_GRASSLANDS, identifier="EVENT_2480_start_battle_3"
        ),
        JmpIfBitSet(
            RUN_AWAY,
            ["EVENT_2480_set_temp_action_script_sync_12"],
            identifier="EVENT_2480_jmp_if_bit_set_4"),
        JmpIfBitSet(GAME_OVER, ["EVENT_2480_reset_and_choose_game_15"]),
        RemoveObjectFromSpecificLevel(NPC_1, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        RemoveObjectFromSpecificLevel(NPC_7, R251_BEAN_VALLEY_PIRANHA_PIPE_AREA),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_7),
        FadeInFromBlack(sync=False),
        Return(),
        SetTempSyncActionScript(
            NPC_7,
            A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES,
            identifier="EVENT_2480_set_temp_action_script_sync_12"),
        FadeInFromBlack(sync=False),
        Return(),
        ResetAndChooseGame(identifier="EVENT_2480_reset_and_choose_game_15"),
        Return(),
    ]
)
