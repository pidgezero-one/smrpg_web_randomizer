# E0046_GRANT_ANY_EQUIP_EXCLUDE_WORST

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToRandom(PRIMARY_TEMP_7000, 3),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_46__2"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_46___2"]),
	JmpToEvent(E0010_SET_70A7_TO_RANDOM_TIER_2_EQUIP),
	JmpToEvent(E0011_SET_70A7_TO_RANDOM_TIER_3_EQUIP, identifier="EVENT_46__2"),
	JmpToEvent(E0012_SET_70A7_TO_RANDOM_TIER_4_EQUIP, identifier="EVENT_46___2")
])
