# E0040_GRANT_ANY_EQUIP_TIER_3_CAP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToRandom(PRIMARY_TEMP_7000, 3),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_40__2"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_40___2"]),
	JmpToEvent(E0009_SET_70A7_TO_RANDOM_TIER_1_EQUIP),
	JmpToEvent(E0010_SET_70A7_TO_RANDOM_TIER_2_EQUIP, identifier="EVENT_40__2"),
	JmpToEvent(E0011_SET_70A7_TO_RANDOM_TIER_3_EQUIP, identifier="EVENT_40___2")
])
