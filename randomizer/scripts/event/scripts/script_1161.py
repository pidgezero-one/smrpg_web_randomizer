# E1161_SEASIDE_LIBERATED_ACCESSORY_SHOP_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitClear(SEASIDE_SHED_EMPTIED, ["EVENT_1161_remove_from_current_level_3"]),
	FadeInFromBlack(sync=False),
	Return(),
	RemoveObjectFromCurrentLevel(NPC_0, identifier="EVENT_1161_remove_from_current_level_3"),
	RemoveObjectFromCurrentLevel(NPC_1),
	FadeInFromBlack(sync=False),
	Return()
])
