# E2412_FOREST_SECRET_TRAMPOLINE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetBit(DIRECTIONAL_7045_3),
	Jmp(["EVENT_2416_set_bit_0"])
])
