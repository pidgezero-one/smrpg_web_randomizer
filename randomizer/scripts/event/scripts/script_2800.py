# E2800_CASINO_EXIT_TO_WORLD_MAP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(TEMP_708C_4, ["EVENT_2800_open_location_3"]),
	ExitToWorldMap(area=OW40_GRATE_GUYS_CASINO, bit_6=True, bit_7=True),
	Return(),
	ExitToWorldMap(area=OW46_GRATE_GUYS_CASINO, bit_6=True, bit_7=True, identifier="EVENT_2800_open_location_3"),
	Return()
])
