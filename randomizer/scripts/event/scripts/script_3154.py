# pylint: disable=C0301

"""E3154_RESUMMON_ROSE_WAY_NPCS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E1603_EXP_STAR_SUBROUTINE_CANCEL_TILE_EVENT),
        ClearBit(TEMP_707C_1),
        SummonObjectToSpecificLevel(NPC_13, R079_ROSE_WAY_MAIN_AREA),
        SummonObjectToSpecificLevel(NPC_14, R079_ROSE_WAY_MAIN_AREA),
        SummonObjectToSpecificLevel(NPC_15, R079_ROSE_WAY_MAIN_AREA),
        SummonObjectToSpecificLevel(NPC_16, R079_ROSE_WAY_MAIN_AREA),
        SummonObjectToSpecificLevel(NPC_3, R080_ROSE_WAY_TWO_FASTFLOATING_PLATFORMS),
        SummonObjectToSpecificLevel(NPC_4, R080_ROSE_WAY_TWO_FASTFLOATING_PLATFORMS),
        SummonObjectToSpecificLevel(NPC_1, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
        SummonObjectToSpecificLevel(NPC_2, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
        SummonObjectToSpecificLevel(NPC_3, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
        SummonObjectToSpecificLevel(NPC_4, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
        SummonObjectToSpecificLevel(NPC_5, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
        SummonObjectToSpecificLevel(NPC_6, R082_ROSE_WAY_WINDING_PATH_WCROOKS),
        SummonObjectToSpecificLevel(NPC_10, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA),
        SummonObjectToSpecificLevel(NPC_11, R081_ROSE_WAY_TREASURE_CHESTS_WCOINS_AREA),
        ExitToWorldMap(area=OW17_ROSE_WAY, bit_6=True, bit_7=True),
        Return(),
    ]
)
