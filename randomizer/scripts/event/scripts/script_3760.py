# E3760_NIMBUS_MEZZANINE_TRAMPOLINE_TO_WORLD_MAP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
	ExitToWorldMap(area=OW49_NIMBUS_LAND, bit_6=True, bit_7=True),
	Return()
])
