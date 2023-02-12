# E2339_TOWER_FIRST_STAIRCASE_CONTROLS_NPC_BEHIND_CURTAIN

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(UNKNOWN_7047_7, ["EVENT_2339_ret_6"]),
        SetBit(UNKNOWN_7047_7),
        SummonObjectToSpecificLevel(
            NPC_4, R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS
        ),
        SummonObjectToSpecificLevel(
            NPC_5, R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS
        ),
        RemoveObjectFromSpecificLevel(
            NPC_6, R193_BOOSTER_TOWER_2F_AREA_03_STEPS_WCIRCLING_BOBOMBS
        ),
        SetSyncActionScript(NPC_6, A0702_TOWER_FIRST_STAIRCASE_BOSS),
        Return(identifier="EVENT_2339_ret_6"),
    ]
)
