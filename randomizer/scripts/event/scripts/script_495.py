# E0495_PIPE_VAULT_PIRANHA_TIMER_3

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7044_0, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7044_0),
	ClearBit(TEMP_7043_7),
	ClearBit(TEMP_7044_1),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_495_clear_bit_8"]),
	ClearBit(TEMP_7044_4),
	SetBit(TEMP_7044_5),
	Return(),
	ClearBit(TEMP_7044_5, identifier="EVENT_495_clear_bit_8"),
	SetBit(TEMP_7044_4),
	Return()
])
