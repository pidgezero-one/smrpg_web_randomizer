# pylint: disable=C0301

"""E1078_MELODY_BAY_FINAL_SONG"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(
            TEMP_7043_0,
            ["EVENT_1078_jmp_if_bit_clear_143"],
            identifier="EVENT_1078_jmp_if_bit_clear_140",
        ),
        SetSyncActionScript(NPC_0, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        JmpIfBitClear(
            TEMP_7043_1,
            ["EVENT_1078_jmp_if_bit_clear_146"],
            identifier="EVENT_1078_jmp_if_bit_clear_143",
        ),
        SetSyncActionScript(NPC_1, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        JmpIfBitClear(
            TEMP_7043_2,
            ["EVENT_1078_jmp_if_bit_clear_149"],
            identifier="EVENT_1078_jmp_if_bit_clear_146",
        ),
        SetSyncActionScript(NPC_2, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        JmpIfBitClear(
            TEMP_7043_3,
            ["EVENT_1078_jmp_if_bit_clear_152"],
            identifier="EVENT_1078_jmp_if_bit_clear_149",
        ),
        SetSyncActionScript(NPC_3, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        JmpIfBitClear(
            TEMP_7043_4,
            ["EVENT_1078_jmp_if_bit_clear_155"],
            identifier="EVENT_1078_jmp_if_bit_clear_152",
        ),
        SetSyncActionScript(NPC_4, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        JmpIfBitClear(
            TEMP_7043_5,
            ["EVENT_1078_jmp_if_bit_clear_158"],
            identifier="EVENT_1078_jmp_if_bit_clear_155",
        ),
        SetSyncActionScript(NPC_5, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        JmpIfBitClear(
            TEMP_7043_6,
            ["EVENT_1078_jmp_if_bit_clear_161"],
            identifier="EVENT_1078_jmp_if_bit_clear_158",
        ),
        SetSyncActionScript(NPC_6, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        JmpIfBitClear(
            TEMP_7043_7,
            ["EVENT_1078_ret_164"],
            identifier="EVENT_1078_jmp_if_bit_clear_161",
        ),
        SetSyncActionScript(NPC_7, A0157_MELODY_BAY_TADPOLES),
        Pause(5),
        Return(identifier="EVENT_1078_ret_164"),
    ]
)
