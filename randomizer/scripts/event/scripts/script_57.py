# E0057_GRANT_ANY_CONSUMABLE_CUSTOM_CAP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CopyVarToVar(from_var=FLAG_COLLECTION_7088, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x0018),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_57_tier4"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_57_tier3"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 16, ["EVENT_57_tier2"]),
	JmpToEvent(E0005_SET_70A7_TO_RANDOM_TIER_1_CONSUMABLE),
	JmpToEvent(E0042_GRANT_ANY_CONSUMABLE_TIER_2_CAP, identifier="EVENT_57_tier2"),
	JmpToEvent(E0041_GRANT_ANY_CONSUMABLE_TIER_3_CAP, identifier="EVENT_57_tier3"),
	JmpToEvent(E0036_GRANT_ANY_CONSUMABLE, identifier="EVENT_57_tier4")
])
