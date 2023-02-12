# E0491_RED_ROOM_PIRANHA_4

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7044_5, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7044_5),
	Return()
])
