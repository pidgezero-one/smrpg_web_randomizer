# pylint: disable=C0301

"""E1573_MIDAS_RIVER_BARREL_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(Z_COORD_2, 0),
        JmpIfBitClear(TEMP_7044_6, ["EVENT_1573_set_7000_to_7000_short_mem_4"]),
        AddConstToVar(X_COORD_2, 1),
        AddConstToVar(Y_COORD_2, 2),
        CopyVarToVar(
            from_var=TEMP_7026,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_1573_set_7000_to_7000_short_mem_4"),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
        ResetCoords(MEM_70A8),
        SetSyncActionScript(MEM_70A8, A0595_MIDAS_BARREL_SLOW_ANIMATION),
        AddConstToVar(PRIMARY_TEMP_7000, 8),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
        SetSyncActionScript(MEM_70A8, A0170_MIDAS_BARRELS_WATER_SPLASH),
        CopyVarToVar(from_var=TEMP_7028, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
        ResetCoords(MEM_70A8),
        ResetCoords(MARIO),
        JmpIfBitSet(TEMP_7044_6, ["EVENT_1573_set_action_script_sync_19"]),
        SetSyncActionScript(MEM_70A8, A0596_MIDAS_BARREL_LEFT_LANE_TO_RIGHT),
        SetSyncActionScript(MARIO, A0596_MIDAS_BARREL_LEFT_LANE_TO_RIGHT),
        Jmp(["EVENT_1573_pause_21"]),
        SetSyncActionScript(
            MEM_70A8,
            A0594_MIDAS_BARREL_RIGHT_LANE_TO_LEFT,
            identifier="EVENT_1573_set_action_script_sync_19"),
        SetSyncActionScript(MARIO, A0594_MIDAS_BARREL_RIGHT_LANE_TO_LEFT),
        Pause(5, identifier="EVENT_1573_pause_21"),
        SetBit(TEMP_7044_3),
        Return(),
    ]
)
