# E0038_GRANT_ANY_CONSUMABLE_OR_EQUIP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToRandom(PRIMARY_TEMP_7000, 4),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_38__2"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_38___2"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_38____2"]),
	JmpToEvent(E0029_GRANT_TIER_4_CONSUMABLE_OR_EQUIP),
	JmpToEvent(E0028_GRANT_TIER_3_CONSUMABLE_OR_EQUIP, identifier="EVENT_38__2"),
	JmpToEvent(E0027_GRANT_TIER_2_CONSUMABLE_OR_EQUIP, identifier="EVENT_38___2"),
	JmpToEvent(E0026_GRANT_TIER_1_CONSUMABLE_OR_EQUIP, identifier="EVENT_38____2")
])
