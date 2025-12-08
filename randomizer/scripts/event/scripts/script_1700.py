# pylint: disable=C0301

"""E1700_BANDITS_WAY_2_LEFT_PLATFORM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_5, ["EVENT_1700_ret_26"]),
        PlaySound(sound=SO058_INSERT, channel=6),
        SetBit(TEMP_7043_5),
        EnableControlsUntilReturn([]),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_1700_pause_action_script_9"]),
        SetBit(TEMP_7043_3),
        SetBit(TEMP_7043_1),
        ClearBit(TEMP_7043_2),
        RunBackgroundEvent(
            event_id=E1705_BANDITS_WAY_2_DOGS_BACKGROUND, return_on_level_exit=True
        ),
        PauseActionScript(NPC_6, identifier="EVENT_1700_pause_action_script_9"),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True, bit_7=True),
        CompareVarToConst(PRIMARY_TEMP_7000, 12),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1700_mem_compare_val_14"]),
        Return(),
        CompareVarToConst(
            PRIMARY_TEMP_7000, 15, identifier="EVENT_1700_mem_compare_val_14"
        ),
        JmpIfComparisonResultIsLesser(["EVENT_1700_set_7000_to_7000_short_mem_17"]),
        Return(),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_1700_set_7000_to_7000_short_mem_17"),
        CompareVarToConst(PRIMARY_TEMP_7000, 26),
        JmpIfLoadedMemoryIsNot0(["EVENT_1700_set_21"]),
        AddConstToVar(SECONDARY_TEMP_7024, 128),
        SetVarToConst(TEMP_70A9, 26, identifier="EVENT_1700_set_21"),
        SetVarToConst(ROSE_WAY_703E, 26),
        SetSyncActionScript(NPC_7, A0478_BANDITS_WAY_1ST_PLATFORMS_SWING),
        Pause(34),
        SetSyncActionScript(NPC_7, A0477_BANDITS_WAY_1ST_PLATFORMS_STATIC),
        Return(identifier="EVENT_1700_ret_26"),
    ]
)
