# E1542_FOREST_MAZE_PIPE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	FreezeAllNPCsUntilReturn(),
	Set7000ToTappedButton(),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_1542_end_all_6"]),
	Set7000ToPressedButton(),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_1542_end_all_6"]),
	Return(),
	EndAll(identifier="EVENT_1542_end_all_6")
])
