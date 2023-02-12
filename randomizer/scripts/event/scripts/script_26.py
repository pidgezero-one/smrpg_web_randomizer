# E0026_GRANT_TIER_1_CONSUMABLE_OR_EQUIP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfRandom2of3(['EVENT_26_3', 'EVENT_26_3']),
	JmpToEvent(E0009_SET_70A7_TO_RANDOM_TIER_1_EQUIP),
	JmpToEvent(E0005_SET_70A7_TO_RANDOM_TIER_1_CONSUMABLE, identifier="EVENT_26_3")
])
