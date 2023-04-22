# pylint: disable=C0301

"""E1783_LANDS_END_FINAL_WHIRLPOOL_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SummonObjectToSpecificLevel(NPC_2, R319_LANDS_END_DESERT_AREA_06),
        SummonObjectToSpecificLevel(NPC_6, R402_LANDS_END_DESERT_AREA_03),
        SummonObjectToSpecificLevel(NPC_2, R403_LANDS_END_DESERT_AREA_05),
        SummonObjectToSpecificLevel(NPC_3, R404_LANDS_END_DESERT_AREA_04),
        SummonObjectToSpecificLevel(NPC_6, R318_LANDS_END_DESERT_AREA_02),
        SummonObjectToSpecificLevel(NPC_0, R263_LANDS_END_UNDERGROUND_AREA_01),
        SummonObjectToSpecificLevel(NPC_1, R263_LANDS_END_UNDERGROUND_AREA_01),
        SummonObjectToSpecificLevel(NPC_2, R263_LANDS_END_UNDERGROUND_AREA_01),
        SummonObjectToSpecificLevel(NPC_0, R264_LANDS_END_UNDERGROUND_AREA_02),
        SummonObjectToSpecificLevel(NPC_1, R264_LANDS_END_UNDERGROUND_AREA_02),
        SummonObjectToSpecificLevel(NPC_2, R264_LANDS_END_UNDERGROUND_AREA_02),
        SummonObjectToSpecificLevel(NPC_0, R265_LANDS_END_UNDERGROUND_AREA_03),
        SummonObjectToSpecificLevel(NPC_1, R265_LANDS_END_UNDERGROUND_AREA_03),
        SummonObjectToSpecificLevel(NPC_2, R265_LANDS_END_UNDERGROUND_AREA_03),
        SummonObjectToSpecificLevel(
            NPC_0, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_1, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_2, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_3, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_4, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_5, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_6, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_7, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_8, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_9, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_10, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_11, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_12, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_13, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_14, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        SummonObjectToSpecificLevel(
            NPC_15, R262_LANDS_END_UNDERGROUND_AREA_04_BUY_SUPER_STARS
        ),
        ClearBit(UNKNOWN_704F_5),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASDb(bytearray(b"\x97\x15")),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[0]),
            ],
        ),
        JmpIfBitSet(TEMP_7044_6, ["EVENT_1783_set_short_35"]),
        RunEventAsSubroutine(E1844_SUMMON_CLOUD_BOSS),
        FadeInFromBlack(sync=False),
        SetVarToConst(SECONDARY_TEMP_7024, 20, identifier="EVENT_1783_set_short_35"),
        SetVarToConst(TEMP_7026, 21),
        SetBit(TEMP_7044_5),
        Return(),
    ]
)
