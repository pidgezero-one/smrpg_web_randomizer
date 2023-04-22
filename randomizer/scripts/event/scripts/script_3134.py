# pylint: disable=C0301

"""E3134_RESUMMON_ENEMIES_IN_SEWER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SummonObjectToSpecificLevel(
            NPC_0,
            R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES,
            identifier="EVENT_3134_summon_to_level_15",
        ),
        SummonObjectToSpecificLevel(
            NPC_1, R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES
        ),
        SummonObjectToSpecificLevel(
            NPC_0, R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER
        ),
        SummonObjectToSpecificLevel(
            NPC_1, R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER
        ),
        SummonObjectToSpecificLevel(
            NPC_2, R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER
        ),
        SummonObjectToSpecificLevel(
            NPC_3, R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER
        ),
        SummonObjectToSpecificLevel(
            NPC_4, R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER
        ),
        SummonObjectToSpecificLevel(
            NPC_5, R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER
        ),
        SummonObjectToSpecificLevel(
            NPC_0, R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE
        ),
        SummonObjectToSpecificLevel(
            NPC_1, R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE
        ),
        SummonObjectToSpecificLevel(
            NPC_2, R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE
        ),
        SummonObjectToSpecificLevel(
            NPC_3, R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE
        ),
        SummonObjectToSpecificLevel(
            NPC_1, R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS
        ),
        SummonObjectToSpecificLevel(
            NPC_2, R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS
        ),
        SummonObjectToSpecificLevel(
            NPC_3, R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS
        ),
        SummonObjectToSpecificLevel(
            NPC_4, R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS
        ),
        SummonObjectToSpecificLevel(
            NPC_5, R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS
        ),
        SummonObjectToSpecificLevel(
            NPC_6, R059_KERO_SEWERS_AREA_05_SUPER_STAR_ROOM_WFOUR_RAT_FUNKS
        ),
        SummonObjectToSpecificLevel(
            NPC_2, R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS
        ),
        SummonObjectToSpecificLevel(
            NPC_3, R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS
        ),
        SummonObjectToSpecificLevel(
            NPC_4, R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS
        ),
        SummonObjectToSpecificLevel(
            NPC_5, R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS
        ),
        SummonObjectToSpecificLevel(
            NPC_6, R060_KERO_SEWERS_AREA_04_LARGE_ROOM_WPANDORITE_AND_HIDING_RAT_FUNKS
        ),
        SummonObjectToSpecificLevel(
            NPC_3, R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS
        ),
        SummonObjectToSpecificLevel(
            NPC_4, R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS
        ),
        SummonObjectToSpecificLevel(
            NPC_5, R301_KERO_SEWERS_AREA_07_WATER_SWITCH_ROOM_WBOOS
        ),
        ClearBit(SEWER_WATER_LEVEL),
        ApplySolidityModToLevel(
            permanent=False,
            room_id=R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES,
            mod_id=0,
        ),
        ApplySolidityModToLevel(
            permanent=False,
            room_id=R056_KERO_SEWERS_AREA_02_LONG_ROOM_WTHREE_PIPES,
            mod_id=1,
        ),
        ApplySolidityModToLevel(
            permanent=False,
            room_id=R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER,
            mod_id=0,
        ),
        ApplySolidityModToLevel(
            permanent=False,
            room_id=R057_KERO_SEWERS_AREA_03_LARGE_WATER_ROOM_WPIPE_IN_CENTER,
            mod_id=1,
        ),
        ApplySolidityModToLevel(
            permanent=False,
            room_id=R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE,
            mod_id=0,
        ),
        ApplySolidityModToLevel(
            permanent=False,
            room_id=R058_KERO_SEWERS_AREA_06_LONG_WATER_ROOM_WRAT_FUNKS_IN_A_LINE,
            mod_id=1,
        ),
        SetBit(TEMP_7042_0),
        Return(),
    ]
)
