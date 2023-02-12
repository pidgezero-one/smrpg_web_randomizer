# E0259_UNKNOWN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitClear(TEMP_7043_0, ["EVENT_256_ret_0"]),
	ClearBit(TEMP_7043_0),
	Return()
])
