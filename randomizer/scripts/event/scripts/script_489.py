# E0489_RED_ROOM_PIRANHA_2

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7044_4, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7044_4),
	Return()
])
