# E1569_MIDAS_RIVER_BARREL_SUBROUTINE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(UNKNOWN_MIDAS_RIVER_7079_0, ["EVENT_1569_set_short_5"]),
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 30),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1569_set_short_5"]),
	Return(),
	SetVarToConst(TEMP_702C, 160, identifier="EVENT_1569_set_short_5"),
	Pause(1, identifier="EVENT_1569_pause_6"),
	Dec(TEMP_702C),
	JmpIfVarNotEqualsConst(TEMP_702C, 0, ["EVENT_1569_pause_6"]),
	JmpIfBitSet(TEMP_7044_2, ["EVENT_1569_set_short_13"]),
	SetSyncActionScript(NPC_0, A0597_MIDAS_FISH),
	SetSyncActionScript(NPC_11, A0167_SPAWN_AT_7016_701A_CALCULATED),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 1, ["EVENT_1569_ret_20"]),
	SetVarToConst(TEMP_702C, 80, identifier="EVENT_1569_set_short_13"),
	Pause(1, identifier="EVENT_1569_pause_14"),
	Dec(TEMP_702C),
	JmpIfVarNotEqualsConst(TEMP_702C, 0, ["EVENT_1569_pause_14"]),
	JmpIfBitSet(TEMP_7044_2, ["EVENT_1569_ret_20"]),
	SetSyncActionScript(NPC_0, A0597_MIDAS_FISH),
	SetSyncActionScript(NPC_11, A0167_SPAWN_AT_7016_701A_CALCULATED),
	Return(identifier="EVENT_1569_ret_20")
])
