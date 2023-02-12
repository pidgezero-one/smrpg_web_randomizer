# E0414_SET_TEMP_7044_0

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7044_0, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7044_0),
	Return()
])
