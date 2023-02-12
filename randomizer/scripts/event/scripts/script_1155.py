# E1155_SEASIDE_LIBERATED_ELDERS_HOUSE_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitClear(SEASIDE_SHED_EMPTIED, ["EVENT_1155_remove_from_current_level_3"]),
	FadeInFromBlack(sync=False),
	Return(),
	RemoveObjectFromCurrentLevel(NPC_0, identifier="EVENT_1155_remove_from_current_level_3"),
	FadeInFromBlack(sync=False),
	Return()
])
