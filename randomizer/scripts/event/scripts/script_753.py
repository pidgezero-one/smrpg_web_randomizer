# E0753_ROSE_TOWN_INNKEEPER_OVER_COUNTER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_7044_0, ["EVENT_256_ret_0"]),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_256_ret_0"]),
	Jmp(["EVENT_289_set_7000_to_current_level_0"])
])
