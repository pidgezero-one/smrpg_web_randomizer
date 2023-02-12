# E0037_GRANT_ANY_EQUIP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToRandom(PRIMARY_TEMP_7000, 4),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_37__2"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_37___2"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_37____2"]),
	JmpToEvent(E0012_SET_70A7_TO_RANDOM_TIER_4_EQUIP),
	JmpToEvent(E0011_SET_70A7_TO_RANDOM_TIER_3_EQUIP, identifier="EVENT_37__2"),
	JmpToEvent(E0010_SET_70A7_TO_RANDOM_TIER_2_EQUIP, identifier="EVENT_37___2"),
	JmpToEvent(E0009_SET_70A7_TO_RANDOM_TIER_1_EQUIP, identifier="EVENT_37____2")
])
