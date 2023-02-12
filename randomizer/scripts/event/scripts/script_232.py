# E0232_FREESTANDING_10_GRANT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 41, ["EVENT_232_room_41_logic"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 422, ["EVENT_232_room_422_logic"]),
	Return(),
	JmpToEvent(E1293_COLLECT_FREESTANDING_SMALL_COIN, identifier="EVENT_232_room_41_logic"),
	JmpToEvent(E3238_FREESTANDING_FROG_COIN, identifier="EVENT_232_room_422_logic")
])
