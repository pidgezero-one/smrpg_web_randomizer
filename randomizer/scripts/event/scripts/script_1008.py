# pylint: disable=C0301

"""E1008_POST_MINES_BOSS_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(RUN_AWAY, ["EVENT_1008_set_temp_action_script_sync_7"]),
        JmpIfBitSet(GAME_OVER, ["EVENT_287_reset_and_choose_game_0"]),
        RemoveObjectAt70A8FromCurrentLevel(),
        RemoveObjectFromCurrentLevel(MEM_70A8),
        JmpIfBitSet(TEMP_704A_2, ["EVENT_1010_clear_bit_7"]),
        FadeInFromBlack(sync=False),
        Return(),
        SetTempSyncActionScript(
            MEM_70A8,
            A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES,
            identifier="EVENT_1008_set_temp_action_script_sync_7"),
        JmpIfBitSet(TEMP_704A_2, ["EVENT_1010_clear_bit_7"]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
