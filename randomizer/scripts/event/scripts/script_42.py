# E0042_GRANT_ANY_CONSUMABLE_TIER_2_CAP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToRandom(PRIMARY_TEMP_7000, 2),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_42__2"]),
	JmpToEvent(E0005_SET_70A7_TO_RANDOM_TIER_1_CONSUMABLE),
	JmpToEvent(E0006_SET_70A7_TO_RANDOM_TIER_2_CONSUMABLE, identifier="EVENT_42__2")
])
