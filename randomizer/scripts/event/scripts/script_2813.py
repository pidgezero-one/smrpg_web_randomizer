# pylint: disable=C0301

"""E2813_MUSHROOM_WAY_3_SUMMON_SPINYS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(3, identifier="EVENT_2813_pause_0"),
        JmpIfBitSet(TEMP_7043_7, ["EVENT_2813_jmp_20"]),
        JmpIfBitClear(TEMP_7043_0, ["EVENT_2813_jmp_20"]),
        ClearBit(TEMP_7043_0),
        JmpIfObjectNotInSpecificLevel(
            NPC_0, R205_MUSHROOM_WAY_AREA_03, ["EVENT_2813_summon_to_level_16"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_1, R205_MUSHROOM_WAY_AREA_03, ["EVENT_2813_summon_to_level_12"]
        ),
        JmpIfObjectNotInSpecificLevel(
            NPC_2, R205_MUSHROOM_WAY_AREA_03, ["EVENT_2813_summon_to_level_8"]
        ),
        Jmp(["EVENT_2813_jmp_20"]),
        SummonObjectToSpecificLevel(
            NPC_2, R205_MUSHROOM_WAY_AREA_03, identifier="EVENT_2813_summon_to_level_8"
        ),
        SetSyncActionScript(NPC_2, A0196_EMPTY),
        SetTempSyncActionScript(NPC_6, A0556_BOOSTER_PASS_LAKITU_TOSSING),
        Jmp(["EVENT_2813_pause_19"]),
        SummonObjectToSpecificLevel(
            NPC_1, R205_MUSHROOM_WAY_AREA_03, identifier="EVENT_2813_summon_to_level_12"
        ),
        SetSyncActionScript(NPC_1, A0196_EMPTY),
        SetTempSyncActionScript(NPC_6, A0556_BOOSTER_PASS_LAKITU_TOSSING),
        Jmp(["EVENT_2813_pause_19"]),
        SummonObjectToSpecificLevel(
            NPC_0, R205_MUSHROOM_WAY_AREA_03, identifier="EVENT_2813_summon_to_level_16"
        ),
        SetSyncActionScript(NPC_0, A0196_EMPTY),
        SetTempSyncActionScript(NPC_6, A0556_BOOSTER_PASS_LAKITU_TOSSING),
        Pause(32, identifier="EVENT_2813_pause_19"),
        Jmp(["EVENT_2813_pause_0"], identifier="EVENT_2813_jmp_20"),
    ]
)
