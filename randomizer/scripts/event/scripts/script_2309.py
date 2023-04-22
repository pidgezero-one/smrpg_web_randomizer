# pylint: disable=C0301

"""E2309_BOOSTER_PASS_LAKITU_TOSSES_SPINY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(3, identifier="EVENT_2309_pause_0"),
        JmpIfBitSet(TEMP_7043_7, ["EVENT_2309_jmp_20"]),
        JmpIfBitClear(TEMP_7043_0, ["EVENT_2309_jmp_20"]),
        ClearBit(TEMP_7043_0),
        JmpIfObjectNotInSpecificLevel(
            NPC_0, R100_BOOSTER_PASS_AREA_01, ["EVENT_2309_summon_to_level_16"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_1, R100_BOOSTER_PASS_AREA_01, ["EVENT_2309_summon_to_level_12"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_2, R100_BOOSTER_PASS_AREA_01, ["EVENT_2309_summon_to_level_8"]
        ),
        Jmp(["EVENT_2309_jmp_20"]),
        SummonObjectToSpecificLevel(
            NPC_2, R100_BOOSTER_PASS_AREA_01, identifier="EVENT_2309_summon_to_level_8"
        ),
        SetSyncActionScript(NPC_2, A0555_BOOSTER_PASS_TOSSED_SPINY),
        SetTempSyncActionScript(NPC_4, A0556_BOOSTER_PASS_LAKITU_TOSSING),
        Jmp(["EVENT_2309_pause_19"]),
        SummonObjectToSpecificLevel(
            NPC_1, R100_BOOSTER_PASS_AREA_01, identifier="EVENT_2309_summon_to_level_12"
        ),
        SetSyncActionScript(NPC_1, A0555_BOOSTER_PASS_TOSSED_SPINY),
        SetTempSyncActionScript(NPC_4, A0556_BOOSTER_PASS_LAKITU_TOSSING),
        Jmp(["EVENT_2309_pause_19"]),
        SummonObjectToSpecificLevel(
            NPC_0, R100_BOOSTER_PASS_AREA_01, identifier="EVENT_2309_summon_to_level_16"
        ),
        SetSyncActionScript(NPC_0, A0555_BOOSTER_PASS_TOSSED_SPINY),
        SetTempSyncActionScript(NPC_4, A0556_BOOSTER_PASS_LAKITU_TOSSING),
        Pause(32, identifier="EVENT_2309_pause_19"),
        Jmp(["EVENT_2309_pause_0"], identifier="EVENT_2309_jmp_20"),
    ]
)
