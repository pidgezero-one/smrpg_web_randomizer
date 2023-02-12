# E0050_GRANT_ANY_EQUIP_OR_CONSUMABLE_EXCLUDE_WORST_TIER_3_CAP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToRandom(PRIMARY_TEMP_7000, 2),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_50__2"]),
	JmpToEvent(E0027_GRANT_TIER_2_CONSUMABLE_OR_EQUIP),
	JmpToEvent(E0028_GRANT_TIER_3_CONSUMABLE_OR_EQUIP, identifier="EVENT_50__2")
])
