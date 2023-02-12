# E3609_KEEP_INVISIBLE_FLOOR_CHESTS

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfVarEqualsConst(ACTIVE_NPC, 25, ["EVENT_3609_chest_2"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 26, ["EVENT_3609_chest_3"]),
	JmpIfVarEqualsConst(ACTIVE_NPC, 27, ["EVENT_3609_chest_4"]),
	JmpToEvent(E1841_KEEP_INVISIBLE_FLOOR_CHEST_1),
	JmpToEvent(E1866_KEEP_INVISIBLE_FLOOR_CHEST_2, identifier="EVENT_3609_chest_2"),
	JmpToEvent(E1870_KEEP_INVISIBLE_FLOOR_CHEST_3, identifier="EVENT_3609_chest_3"),
	JmpToEvent(E1880_KEEP_INVISIBLE_FLOOR_CHEST_4, identifier="EVENT_3609_chest_4")
])
