# E1162_SEASIDE_LIBERATED_SHED_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(SEASIDE_SHED_EMPTIED, ["EVENT_1162_remove_from_current_level_3"]),
	FadeInFromBlack(sync=False),
	Jmp(["EVENT_1178_pause_0"]),
	RemoveObjectFromCurrentLevel(NPC_0, identifier="EVENT_1162_remove_from_current_level_3"),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	RemoveObjectFromCurrentLevel(NPC_5),
	RemoveObjectFromCurrentLevel(NPC_6),
	FadeInFromBlack(sync=False),
	Return()
])
