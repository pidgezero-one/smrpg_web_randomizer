# E3825_NIMBUS_FINAL_CHEST_ROOM_PLATFORM_BIT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitClear(TEMP_7043_1, ["EVENT_3584_ret_0"]),
	ClearBit(TEMP_7043_1),
	Return()
])
