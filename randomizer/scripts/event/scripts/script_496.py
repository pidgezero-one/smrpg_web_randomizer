# E0496_PIPE_VAULT_PIRANHA_TIMER_4

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7044_1, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7044_1),
	ClearBit(TEMP_7044_0),
	ClearBit(TEMP_7044_2),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_496_clear_bit_8"]),
	ClearBit(TEMP_7044_5),
	SetBit(TEMP_7044_6),
	Return(),
	ClearBit(TEMP_7044_6, identifier="EVENT_496_clear_bit_8"),
	SetBit(TEMP_7044_5),
	Return()
])
