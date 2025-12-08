# pylint: disable=C0301

"""E2335_TOWER_FIRST_STAIRCASE_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(SPOOKUM_DIRECTION),
        JmpIfBitClear(UNUSED_708D_2, ["EVENT_2335_remove_from_level_3"]),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[ASSetSpriteSequence(index=4, is_sequence=True, looping=True)]),
        RemoveObjectFromSpecificLevel(
            NPC_0,
            R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
            identifier="EVENT_2335_remove_from_level_3"),
        RemoveObjectFromSpecificLevel(
            NPC_1, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS
        ),
        RemoveObjectFromSpecificLevel(
            NPC_3, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS
        ),
        RemoveObjectFromSpecificLevel(
            NPC_4, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS
        ),
        RemoveObjectFromSpecificLevel(
            NPC_5, R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS
        ),
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromCurrentLevel(NPC_3),
        RemoveObjectFromCurrentLevel(NPC_4),
        RemoveObjectFromCurrentLevel(NPC_5),
        SetBit(TEMP_707C_5),
        SetBit(TEMP_707C_6),
        SetBit(TEMP_707C_7),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 17, ["EVENT_2335_run_background_event_23"]
        ),
        RunBackgroundEvent(
            event_id=E2336_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_1,
            return_on_level_exit=True),
        FadeInFromBlack(sync=False),
        Return(),
        RunBackgroundEvent(
            event_id=E2337_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_2,
            return_on_level_exit=True,
            identifier="EVENT_2335_run_background_event_23"),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
