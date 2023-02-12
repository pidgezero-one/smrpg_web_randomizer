# E2807_MUSHROOM_WAY_3_EXIT_TO_WORLD_MAP

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TOAD_IN_MUSHROOM_WAY_3, ["EVENT_2808_jmp_if_bit_set_0"]),
        SummonObjectToSpecificLevel(NPC_2, R203_MUSHROOM_WAY_AREA_01),
        SummonObjectToSpecificLevel(NPC_3, R203_MUSHROOM_WAY_AREA_01),
        SummonObjectToSpecificLevel(NPC_4, R203_MUSHROOM_WAY_AREA_01),
        SummonObjectToSpecificLevel(NPC_5, R203_MUSHROOM_WAY_AREA_01),
        SummonObjectToSpecificLevel(NPC_6, R203_MUSHROOM_WAY_AREA_01),
        SummonObjectToSpecificLevel(NPC_7, R203_MUSHROOM_WAY_AREA_01),
        SummonObjectToSpecificLevel(NPC_2, R204_MUSHROOM_WAY_AREA_02),
        SummonObjectToSpecificLevel(NPC_3, R204_MUSHROOM_WAY_AREA_02),
        SummonObjectToSpecificLevel(NPC_4, R204_MUSHROOM_WAY_AREA_02),
        SummonObjectToSpecificLevel(NPC_5, R204_MUSHROOM_WAY_AREA_02),
        SummonObjectToSpecificLevel(NPC_6, R204_MUSHROOM_WAY_AREA_02),
        SummonObjectToSpecificLevel(NPC_9, R204_MUSHROOM_WAY_AREA_02),
        ExitToWorldMap(area=OW09_MUSHROOM_WAY, bit_6=True, bit_7=True),
        Return(),
    ]
)
