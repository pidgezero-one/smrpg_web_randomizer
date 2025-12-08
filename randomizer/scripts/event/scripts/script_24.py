# pylint: disable=C0301

"""E0024_BATTLE_RESULT_CHECK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(RUN_AWAY, ["EVENT_24_set_temp_action_script_sync_18"]),
        JmpIfBitSet(GAME_OVER, ["EVENT_24_reset_and_choose_game_17"]),
        JmpIfBitClear(
            TEMP_707C_6,
            ["EVENT_24_jmp_if_bit_clear_5"],
            identifier="EVENT_24_jmp_if_bit_clear_2"),
        RemoveObjectAt70A8FromCurrentLevel(),
        Pause(1),
        JmpIfBitClear(
            TEMP_707C_7,
            ["EVENT_24_jmp_if_var_not_equals_const_9"],
            identifier="EVENT_24_jmp_if_bit_clear_5"),
        DisableObjectTrigger(MEM_70A8),
        RemoveObjectFromCurrentLevel(MEM_70A8),
        Pause(1),
        JmpIfVarNotEqualsConst(
            GAME_OVER_COUNTER_MAYBE,
            255,
            ["EVENT_24_inc_11"],
            identifier="EVENT_24_jmp_if_var_not_equals_const_9"),
        SetVarToConst(GAME_OVER_COUNTER_MAYBE, 0),
        Inc(GAME_OVER_COUNTER_MAYBE, identifier="EVENT_24_inc_11"),
        JmpIfBitSet(TEMP_707C_5, ["EVENT_24_clear_bit_14"]),
        FadeInFromBlack(sync=False),
        ClearBit(TEMP_707C_5, identifier="EVENT_24_clear_bit_14"),
        ReactivateObject70A8TriggerIfMarioOnTopOfIt(
            identifier="EVENT_24_reactivate_trigger_if_mario_on_top_of_object_15"
        ),
        Return(),
        ResetAndChooseGame(identifier="EVENT_24_reset_and_choose_game_17"),
        SetTempSyncActionScript(
            MEM_70A8,
            A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES,
            identifier="EVENT_24_set_temp_action_script_sync_18"),
        JmpIfBitSet(TEMP_707C_5, ["EVENT_24_clear_bit_14"]),
        FadeInFromBlack(sync=False),
        Jmp(["EVENT_24_reactivate_trigger_if_mario_on_top_of_object_15"]),
    ]
)
