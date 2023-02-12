# E1917_ABYSS_BIG_CONVEYOR_CHECKPOINT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_2, ["EVENT_1917_ret_7"]),
	SetBit(TEMP_7043_2),
	SetVarToConst(TEMP_7026, 3),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_3),
	ClearBit(TEMP_7043_4),
	Return(identifier="EVENT_1917_ret_7")
])
