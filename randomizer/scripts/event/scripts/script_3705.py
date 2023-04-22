# pylint: disable=C0301

"""E3705_JAWFUL_BATTLE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(
            E1604_EXP_STAR_SUBROUTINE_CANCEL_NPC_EVENT_REMOVE_FROM_LEVEL
        ),
        StartBattleAtBattlefield(99, BF22_NIMBUS_CASTLE),
        JmpIfBitSet(RUN_AWAY, ["EVENT_3705_set_temp_action_script_sync_7"]),
        JmpIfBitSet(GAME_OVER, ["EVENT_3705_jmp_to_event_18"]),
        RemoveObjectAt70A8FromCurrentLevel(),
        RemoveObjectFromCurrentLevel(MEM_70A8),
        FadeInFromBlack(sync=False),
        Return(),
        SetSyncActionScript(
            MEM_70A8,
            A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES,
            identifier="EVENT_3705_set_temp_action_script_sync_7",
        ),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 410, ["EVENT_3705_set_temp_action_script_sync_14"]
        ),
        SetSyncActionScript(NPC_5, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
        SetSyncActionScript(NPC_6, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
        FadeInFromBlack(sync=False),
        Return(),
        SetSyncActionScript(
            NPC_6,
            A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES,
            identifier="EVENT_3705_set_temp_action_script_sync_14",
        ),
        SetSyncActionScript(NPC_7, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
        FadeInFromBlack(sync=False),
        Return(),
        JmpToEvent(E0287_RESET_GAME, identifier="EVENT_3705_jmp_to_event_18"),
    ]
)
