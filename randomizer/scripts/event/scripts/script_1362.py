# E1362_CURTAIN_3

from randomizer.scripts.event.script_imports import *

script = EventScript([
	MoveScriptToBackgroundThread2(),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_1362_ret_6"]),
	SetBit(TEMP_7043_2),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_3),
	Return(identifier="EVENT_1362_ret_6")
])
