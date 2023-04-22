# pylint: disable=C0301

"""E1786_LANDS_END_SHY_AWAY_WHIRLPOOL_1_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MOUSE_RETURNED_TO_MONSTRO, ["EVENT_1786_summon_to_level_2"]),
        SummonObjectToSpecificLevel(NPC_1, R317_LANDS_END_DESERT_AREA_01),
        SummonObjectToSpecificLevel(
            NPC_2,
            R319_LANDS_END_DESERT_AREA_06,
            identifier="EVENT_1786_summon_to_level_2",
        ),
        SummonObjectToSpecificLevel(NPC_6, R402_LANDS_END_DESERT_AREA_03),
        SummonObjectToSpecificLevel(NPC_2, R403_LANDS_END_DESERT_AREA_05),
        SummonObjectToSpecificLevel(NPC_3, R404_LANDS_END_DESERT_AREA_04),
        SummonObjectToSpecificLevel(NPC_6, R318_LANDS_END_DESERT_AREA_02),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASDb(bytearray(b"\x97\x16")),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[0]),
            ],
        ),
        JmpIfBitSet(TEMP_7044_6, ["EVENT_1786_set_short_11"]),
        RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
        FadeInFromBlack(sync=False),
        SetVarToConst(SECONDARY_TEMP_7024, 20, identifier="EVENT_1786_set_short_11"),
        SetBit(TEMP_7044_5),
        Return(),
    ]
)
