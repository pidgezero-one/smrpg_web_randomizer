# E0508_UNKNOWN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitClear(TEMP_7043_3, ["EVENT_256_ret_0"]),
	ClearBit(TEMP_7043_3),
	Return()
])
