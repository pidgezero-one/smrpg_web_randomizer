# pylint: disable=C0301

"""E2351_TOWER_START_BULLET_BILLS_ANIMATION"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(1, identifier="EVENT_2351_pause_0"),
        JmpIfBitClear(TEMP_7043_3, ["EVENT_2351_pause_0"]),
        ClearBit(TEMP_7043_3),
        JmpIfObjectInCurrentLevel(NPC_8, ["EVENT_2351_ret_40"]),
        JmpIfObjectInCurrentLevel(NPC_0, ["EVENT_2351_reset_coords_6"]),
        Jmp(["EVENT_2351_jmp_if_present_in_current_level_13"]),
        ResetCoords(NPC_0, identifier="EVENT_2351_reset_coords_6"),
        SetSyncActionScript(NPC_0, A0389_TOWER_BULLET_BILL_APPEARS),
        Pause(16),
        SummonObjectToCurrentLevel(NPC_7),
        Pause(8),
        RemoveObjectFromCurrentLevel(NPC_7),
        Jmp(["EVENT_2351_pause_0"]),
        JmpIfObjectInCurrentLevel(
            NPC_1,
            ["EVENT_2351_reset_coords_15"],
            identifier="EVENT_2351_jmp_if_present_in_current_level_13",
        ),
        Jmp(["EVENT_2351_jmp_if_present_in_current_level_22"]),
        ResetCoords(NPC_1, identifier="EVENT_2351_reset_coords_15"),
        SetSyncActionScript(NPC_1, A0389_TOWER_BULLET_BILL_APPEARS),
        Pause(16),
        SummonObjectToCurrentLevel(NPC_7),
        Pause(8),
        RemoveObjectFromCurrentLevel(NPC_7),
        Jmp(["EVENT_2351_pause_0"]),
        JmpIfObjectInCurrentLevel(
            NPC_2,
            ["EVENT_2351_reset_coords_24"],
            identifier="EVENT_2351_jmp_if_present_in_current_level_22",
        ),
        Jmp(["EVENT_2351_jmp_if_present_in_current_level_31"]),
        ResetCoords(NPC_2, identifier="EVENT_2351_reset_coords_24"),
        SetSyncActionScript(NPC_2, A0389_TOWER_BULLET_BILL_APPEARS),
        Pause(16),
        SummonObjectToCurrentLevel(NPC_7),
        Pause(8),
        RemoveObjectFromCurrentLevel(NPC_7),
        Jmp(["EVENT_2351_pause_0"]),
        JmpIfObjectInCurrentLevel(
            NPC_3,
            ["EVENT_2351_reset_coords_33"],
            identifier="EVENT_2351_jmp_if_present_in_current_level_31",
        ),
        Jmp(["EVENT_2351_jmp_39"]),
        ResetCoords(NPC_3, identifier="EVENT_2351_reset_coords_33"),
        SetSyncActionScript(NPC_3, A0389_TOWER_BULLET_BILL_APPEARS),
        Pause(16),
        SummonObjectToCurrentLevel(NPC_7),
        Pause(8),
        RemoveObjectFromCurrentLevel(NPC_7),
        Jmp(["EVENT_2351_pause_0"], identifier="EVENT_2351_jmp_39"),
        Return(identifier="EVENT_2351_ret_40"),
    ]
)
