# E2415_FOREST_UNDERGROUND_1_ENTRANCE_TRAMPOLINE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(DIRECTIONAL_7045_0),
	ClearBit(DIRECTIONAL_7045_1),
	Jmp(["EVENT_2416_set_bit_0"])
])
