# E2414_FOREST_UNDERGROUND_1_EXIT_TRAMPOLINE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(DIRECTIONAL_7045_1),
	ClearBit(DIRECTIONAL_7045_0),
	Jmp(["EVENT_2416_set_bit_0"])
])
