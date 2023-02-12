# E0266_UNKNOWN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	CopyVarToVar(from_var=GAME_OVER_COUNTER_MAYBE, to_var=PRIMARY_TEMP_7000),
	Compare7000ToVar(TEMP_702E),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_266_clear_bit_6"]),
	SetBit(TEMP_7044_0),
	Jmp(["EVENT_256_ret_0"]),
	ClearBit(TEMP_7044_0, identifier="EVENT_266_clear_bit_6"),
	Return()
])
