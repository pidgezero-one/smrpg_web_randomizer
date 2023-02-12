# E0056_GRANT_BEST_EQUIP_OR_CONSUMABLE_CUSTOM_CAP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CopyVarToVar(from_var=FLAG_COLLECTION_7088, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x0018),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_56_tier4"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_56_tier3"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 16, ["EVENT_56_tier2"]),
	JmpToEvent(E0026_GRANT_TIER_1_CONSUMABLE_OR_EQUIP),
	JmpToEvent(E0027_GRANT_TIER_2_CONSUMABLE_OR_EQUIP, identifier="EVENT_56_tier2"),
	JmpToEvent(E0028_GRANT_TIER_3_CONSUMABLE_OR_EQUIP, identifier="EVENT_56_tier3"),
	JmpToEvent(E0029_GRANT_TIER_4_CONSUMABLE_OR_EQUIP, identifier="EVENT_56_tier4")
])
