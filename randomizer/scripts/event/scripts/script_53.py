# E0053_GRANT_ANY_EQUIP_OR_CONSUMABLE_EXCLUDE_WORST_CUSTOM_CAP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	CopyVarToVar(from_var=FLAG_COLLECTION_7088, to_var=PRIMARY_TEMP_7000),
	Mem7000AndConst(0x0018),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_53_tier4"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_53_tier3"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 16, ["EVENT_53_tier2"]),
	JmpToEvent(E0026_GRANT_TIER_1_CONSUMABLE_OR_EQUIP),
	JmpToEvent(E0027_GRANT_TIER_2_CONSUMABLE_OR_EQUIP, identifier="EVENT_53_tier2"),
	JmpToEvent(E0050_GRANT_ANY_EQUIP_OR_CONSUMABLE_EXCLUDE_WORST_TIER_3_CAP, identifier="EVENT_53_tier3"),
	JmpToEvent(E0047_GRANT_ANY_CONSUMABLE_OR_EQUIP_EXCLUDE_WORST, identifier="EVENT_53_tier4")
])
