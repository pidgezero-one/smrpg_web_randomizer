# E0488_RED_ROOM_PIRANHA_1

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitClear(TEMP_7044_4, ["EVENT_256_ret_0"]),
	ClearBit(TEMP_7044_4),
	Return()
])
