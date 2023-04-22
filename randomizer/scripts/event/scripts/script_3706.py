# pylint: disable=C0301

"""E3706_ACTIVATE_JAWFUL_EXTENDED_HITBOXES"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
        JmpIfBitClear(TEMP_7043_0, ["EVENT_3584_ret_0"]),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 114, ["EVENT_3706_jmp_if_object_not_in_level_15"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_5,
            R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE,
            ["EVENT_3584_ret_0"],
        ),
        StartBattleAtBattlefield(99, BF22_NIMBUS_CASTLE),
        JmpIfBitSet(GAME_OVER, ["EVENT_3705_jmp_to_event_18"]),
        JmpIfBitSet(RUN_AWAY, ["EVENT_3706_set_temp_action_script_sync_27"]),
        RemoveObjectFromCurrentLevel(NPC_5),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromCurrentLevel(NPC_7),
        RemoveObjectFromSpecificLevel(
            NPC_5, R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_6, R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE
        ),
        RemoveObjectFromSpecificLevel(
            NPC_7, R410_NIMBUS_CASTLE_AREA_07_STRAIGHT_FROM_AREA_06_WLONG_STAIRCASE
        ),
        FadeInFromBlack(sync=False),
        Return(),
        JmpIfObjectNotInSpecificLevel(
            NPC_4,
            R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
            ["EVENT_3584_ret_0"],
            identifier="EVENT_3706_jmp_if_object_not_in_level_15",
        ),
        StartBattleAtBattlefield(99, BF22_NIMBUS_CASTLE),
        JmpIfBitSet(GAME_OVER, ["EVENT_3705_jmp_to_event_18"]),
        JmpIfBitSet(RUN_AWAY, ["EVENT_3706_set_temp_action_script_sync_27"]),
        RemoveObjectFromCurrentLevel(NPC_4),
        RemoveObjectFromCurrentLevel(NPC_5),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromSpecificLevel(
            NPC_4,
            R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
        ),
        RemoveObjectFromSpecificLevel(
            NPC_5,
            R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
        ),
        RemoveObjectFromSpecificLevel(
            NPC_6,
            R114_NIMBUS_CASTLE_AREA_10_RED_BRICK_2LEVEL_ROOM_WTREASURE_FROM_BIRDOS_ROOM,
        ),
        FadeInFromBlack(sync=False),
        Return(),
        SetSyncActionScript(
            MEM_70A8,
            A0889_JAWFUL_EXTENDED_HITBOXES,
            identifier="EVENT_3706_set_temp_action_script_sync_27",
        ),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 410, ["EVENT_3706_set_temp_action_script_sync_33"]
        ),
        SetSyncActionScript(NPC_4, A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES),
        FadeInFromBlack(sync=False),
        Return(),
        SetSyncActionScript(
            NPC_5,
            A0002_FLASH_AFTER_RUNNING_AWAY_IFRAMES,
            identifier="EVENT_3706_set_temp_action_script_sync_33",
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
