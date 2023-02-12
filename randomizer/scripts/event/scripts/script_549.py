# E0549_ROSE_TOWN_OCCUPIED_ARROW_CONTROL_2

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_256_ret_0"]),
	SetBit(TEMP_7044_6),
	SetBit(TEMP_7044_2),
	Return()
])
