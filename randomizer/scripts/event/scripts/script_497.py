# E0497_PIPE_VAULT_PIRANHA_TIMER_5

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7044_6, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7044_6),
	ClearBit(TEMP_7044_5),
	Return()
])
