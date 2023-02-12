# E0507_PIPE_VAULT_PIRANHA_BIT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7043_3, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7043_3),
	Return()
])
