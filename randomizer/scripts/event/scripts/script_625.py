# E0625_MARRYMORE_INN_SOMETHING

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitClear(TEMP_7044_5, ["EVENT_256_ret_0"]),
	ClearBit(TEMP_7044_5),
	Return()
])
