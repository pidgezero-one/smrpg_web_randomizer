# E2337_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_2

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_0,
            R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
            ["EVENT_2337_summon_to_level_9"],
            identifier="EVENT_2337_jmp_if_object_not_in_level_0",
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
            ["EVENT_2337_summon_to_level_13"],
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_2,
            R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
            ["EVENT_2337_summon_to_level_17"],
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_3,
            R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
            ["EVENT_2337_summon_to_level_21"],
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_4,
            R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
            ["EVENT_2337_summon_to_level_25"],
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_5,
            R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
            ["EVENT_2337_summon_to_level_29"],
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_5,
            R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
            ["EVENT_2337_summon_to_level_29"],
        ),
        Pause(16),
        Jmp(["EVENT_2337_jmp_if_object_not_in_level_0"]),
        SummonObjectToSpecificLevel(
            NPC_0,
            R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
            identifier="EVENT_2337_summon_to_level_9",
        ),
        SetSyncActionScript(NPC_0, A0695_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_2),
        Pause(112),
        Jmp(["EVENT_2337_jmp_if_object_not_in_level_0"]),
        SummonObjectToSpecificLevel(
            NPC_1,
            R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
            identifier="EVENT_2337_summon_to_level_13",
        ),
        SetSyncActionScript(NPC_1, A0695_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_2),
        Pause(112),
        Jmp(["EVENT_2337_jmp_if_object_not_in_level_0"]),
        SummonObjectToSpecificLevel(
            NPC_2,
            R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
            identifier="EVENT_2337_summon_to_level_17",
        ),
        SetSyncActionScript(NPC_2, A0695_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_2),
        Pause(112),
        Jmp(["EVENT_2337_jmp_if_object_not_in_level_0"]),
        SummonObjectToSpecificLevel(
            NPC_3,
            R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
            identifier="EVENT_2337_summon_to_level_21",
        ),
        SetSyncActionScript(NPC_3, A0695_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_2),
        Pause(112),
        Jmp(["EVENT_2337_jmp_if_object_not_in_level_0"]),
        SummonObjectToSpecificLevel(
            NPC_4,
            R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
            identifier="EVENT_2337_summon_to_level_25",
        ),
        SetSyncActionScript(NPC_4, A0695_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_2),
        Pause(112),
        Jmp(["EVENT_2337_jmp_if_object_not_in_level_0"]),
        SummonObjectToSpecificLevel(
            NPC_5,
            R196_BOOSTER_TOWER_2F_AREA_01_WCONSTANTLY_APPEARING_SPOOKUMS,
            identifier="EVENT_2337_summon_to_level_29",
        ),
        SetSyncActionScript(NPC_5, A0695_TOWER_FIRST_STAIRCASE_SPOOKUM_DIRECTION_2),
        Pause(112),
        Jmp(["EVENT_2337_jmp_if_object_not_in_level_0"]),
    ]
)
