# pylint: disable=C0301

"""E1785_LANDS_END_FINAL_WHIRLPOOL_1_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SummonObjectToSpecificLevel(NPC_2, R319_LANDS_END_DESERT_AREA_06),
        SummonObjectToSpecificLevel(NPC_6, R402_LANDS_END_DESERT_AREA_03),
        SummonObjectToSpecificLevel(NPC_2, R403_LANDS_END_DESERT_AREA_05),
        SummonObjectToSpecificLevel(NPC_3, R404_LANDS_END_DESERT_AREA_04),
        SummonObjectToSpecificLevel(NPC_6, R318_LANDS_END_DESERT_AREA_02),
        SetBit(UNKNOWN_704F_6),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASDb(bytearray(b"\x97\x14")),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[1]),
            ],
        ),
        JmpIfBitSet(TEMP_7044_6, ["EVENT_1785_set_short_10"]),
        RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
        FadeInFromBlack(sync=False),
        SetVarToConst(SECONDARY_TEMP_7024, 20, identifier="EVENT_1785_set_short_10"),
        SetVarToConst(TEMP_7026, 20),
        SetBit(TEMP_7044_5),
        Return(),
    ]
)
