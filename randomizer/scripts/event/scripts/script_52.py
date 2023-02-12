# E0052_GRANT_ANY_EQUIP_EXCLUDE_WORST_CUSTOM_CAP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CopyVarToVar(from_var=FLAG_COLLECTION_7088, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x0018),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_52_tier4"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_52_tier3"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 16, ["EVENT_52_tier2"]),
	JmpToEvent(E0009_SET_70A7_TO_RANDOM_TIER_1_EQUIP),
	JmpToEvent(E0010_SET_70A7_TO_RANDOM_TIER_2_EQUIP, identifier="EVENT_52_tier2"),
	JmpToEvent(E0049_GRANT_ANY_EQUIP_EXCLUDE_WORST_TIER_3_CAP, identifier="EVENT_52_tier3"),
	JmpToEvent(E0046_GRANT_ANY_EQUIP_EXCLUDE_WORST, identifier="EVENT_52_tier4")
])
