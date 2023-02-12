# E0039_GRANT_ANY_CONSUMABLE_OR_EQUIP_TIER_3_CAP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToRandom(PRIMARY_TEMP_7000, 3),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_39__2"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_39___2"]),
	JmpToEvent(E0026_GRANT_TIER_1_CONSUMABLE_OR_EQUIP),
	JmpToEvent(E0028_GRANT_TIER_3_CONSUMABLE_OR_EQUIP, identifier="EVENT_39__2"),
	JmpToEvent(E0027_GRANT_TIER_2_CONSUMABLE_OR_EQUIP, identifier="EVENT_39___2")
])
