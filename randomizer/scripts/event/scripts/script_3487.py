# pylint: disable=C0301

"""E3487_MIDAS_RIVER_FROG_COIN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        SetSyncActionScript(MEM_70A8, A0719_MIDAS_RIVER_FROG_COIN),
        AddFrogCoins(1),
        Set7000ToObjectCoord(target_npc=NPC_1, coord=COORD_Y, pixel=True),
        CompareVarToConst(PRIMARY_TEMP_7000, 12288),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3487_set_bit_16"]),
        CompareVarToConst(PRIMARY_TEMP_7000, 8704),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3487_set_bit_14"]),
        CompareVarToConst(PRIMARY_TEMP_7000, 5120),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3487_set_bit_12"]),
        SetBit(UNKNOWN_MIDAS_RIVER_7079_4),
        Return(),
        SetBit(UNKNOWN_MIDAS_RIVER_7079_5, identifier="EVENT_3487_set_bit_12"),
        Return(),
        SetBit(UNKNOWN_MIDAS_RIVER_7079_6, identifier="EVENT_3487_set_bit_14"),
        Return(),
        SetBit(UNKNOWN_MIDAS_RIVER_7079_7, identifier="EVENT_3487_set_bit_16"),
        Return(),
    ]
)
