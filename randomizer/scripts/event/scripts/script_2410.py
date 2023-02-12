# E2410_FOREST_TREE_GENERIC_UNDERGROUND_TRAMPOLINE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	ClearBit(DIRECTIONAL_7046_7),
	ClearBit(DIRECTIONAL_7046_5),
	ClearBit(DIRECTIONAL_7046_6),
	SetBit(DIRECTIONAL_7045_5),
	Jmp(["EVENT_2416_set_bit_0"])
])
