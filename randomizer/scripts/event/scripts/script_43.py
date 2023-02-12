# E0043_GRANT_ANY_EQUIP_TIER_2_CAP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToRandom(PRIMARY_TEMP_7000, 2),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_43__2"]),
	JmpToEvent(E0009_SET_70A7_TO_RANDOM_TIER_1_EQUIP),
	JmpToEvent(E0010_SET_70A7_TO_RANDOM_TIER_2_EQUIP, identifier="EVENT_43__2")
])
