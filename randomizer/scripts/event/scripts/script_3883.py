# E3883_INNER_FACTORY_EXIT_TRAMPOLINE

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	ExitToWorldMap(area=OW01_INNER_FACTORY, bit_6=True, bit_7=True)
])
