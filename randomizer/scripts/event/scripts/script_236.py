# E0236_FREESTANDING_6_GRANT

from randomizer.scripts.event.script_imports import *

script = EventScript([
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 41, ["EVENT_236_room_41_logic"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 79, ["EVENT_236_room_79_logic"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 125, ["EVENT_236_room_125_logic"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 422, ["EVENT_236_room_422_logic"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 457, ["EVENT_236_room_457_logic"]),
	Return(),
	JmpToEvent(E1293_COLLECT_FREESTANDING_SMALL_COIN, identifier="EVENT_236_room_41_logic"),
	JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_236_room_79_logic"),
	JmpToEvent(E3238_FREESTANDING_FROG_COIN, identifier="EVENT_236_room_125_logic"),
	JmpToEvent(E3238_FREESTANDING_FROG_COIN, identifier="EVENT_236_room_422_logic"),
	JmpToEvent(E3146_FREESTANDING_BIG_COIN, identifier="EVENT_236_room_457_logic")
])
