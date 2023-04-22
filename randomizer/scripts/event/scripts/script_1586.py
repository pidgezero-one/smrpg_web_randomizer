# pylint: disable=C0301

"""E1586_MIDAS_RIVER_BARREL_FISH_MOVEMENT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(UNKNOWN_MIDAS_RIVER_7079_0, ["EVENT_1586_set_5"]),
        CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 30),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1586_set_5"]),
        Return(),
        SetVarToConst(PRIMARY_TEMP_7000, 161, identifier="EVENT_1586_set_5"),
        JmpIfBitClear(TEMP_7043_4, ["EVENT_1586_set_7000_short_mem_to_7000_8"]),
        AddConstToVar(PRIMARY_TEMP_7000, 65522),
        CopyVarToVar(
            from_var=PRIMARY_TEMP_7000,
            to_var=TEMP_702C,
            identifier="EVENT_1586_set_7000_short_mem_to_7000_8",
        ),
        Pause(1, identifier="EVENT_1586_pause_9"),
        JmpIfBitSet(TEMP_7044_2, ["EVENT_1586_pause_9"]),
        Dec(TEMP_702C),
        JmpIfVarNotEqualsConst(TEMP_702C, 0, ["EVENT_1586_pause_9"]),
        SetSyncActionScript(NPC_0, A0597_MIDAS_FISH),
        SetSyncActionScript(NPC_11, A0167_SPAWN_AT_7016_701A_CALCULATED),
        Return(),
    ]
)
