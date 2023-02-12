# E0044_GRANT_ANY_CONSUMABLE_OR_EQUIP_TIER_2_CAP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToRandom(PRIMARY_TEMP_7000, 2),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_44__2"]),
	JmpToEvent(E0026_GRANT_TIER_1_CONSUMABLE_OR_EQUIP),
	JmpToEvent(E0027_GRANT_TIER_2_CONSUMABLE_OR_EQUIP, identifier="EVENT_44__2")
])
