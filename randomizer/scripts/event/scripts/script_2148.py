# E2148_KEEP_MOVE_GOOMBAS_IN_ORIGINAL_THRONE_ROOM

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_0, ["EVENT_2148_ret_2"]),
	SetBit(TEMP_7043_0),
	Return(identifier="EVENT_2148_ret_2")
])
