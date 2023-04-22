# pylint: disable=C0301

"""E1784_LANDS_END_DESERT_1_LEFT_WHIRLPOOL_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SummonObjectToSpecificLevel(NPC_2, R319_LANDS_END_DESERT_AREA_06),
        SummonObjectToSpecificLevel(NPC_6, R402_LANDS_END_DESERT_AREA_03),
        SummonObjectToSpecificLevel(NPC_2, R403_LANDS_END_DESERT_AREA_05),
        SummonObjectToSpecificLevel(NPC_3, R404_LANDS_END_DESERT_AREA_04),
        SummonObjectToSpecificLevel(NPC_6, R318_LANDS_END_DESERT_AREA_02),
        ActionQueueAsync(
            target=NPC_6,
            subscript=[
                ASDb(bytearray(b"\x97\x17")),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[0, 1]),
            ],
        ),
        JmpIfBitSet(TEMP_7044_6, ["EVENT_1784_set_short_9"]),
        RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
        FadeInFromBlack(sync=False),
        SetVarToConst(SECONDARY_TEMP_7024, 23, identifier="EVENT_1784_set_short_9"),
        SetBit(TEMP_7044_5),
        Return(),
    ]
)
