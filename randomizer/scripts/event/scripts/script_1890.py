# E1890_DETERMINE_SIDE_TREASURE_ROOM_TO_LOAD

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(ABYSS_TWO_CHEST_ROOM_DIRECTIONAL_BIT, ["EVENT_1890_remove_from_current_level_5"]),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_3),
	FadeInFromBlack(sync=False),
	Return(),
	RemoveObjectFromCurrentLevel(NPC_0, identifier="EVENT_1890_remove_from_current_level_5"),
	RemoveObjectFromCurrentLevel(NPC_2),
	FadeInFromBlack(sync=False),
	Return()
])
