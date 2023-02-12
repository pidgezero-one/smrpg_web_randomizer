# E0568_ROSE_ROWN_LIBERATED_WATER_PUMP_HOUSE_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitSet(ROSE_TOWN_WATER_PUMPERS_POSITION, ["EVENT_568_remove_from_current_level_2"]),
	JmpToEvent(E0261_FADE_MUSIC_ROOM_LOADER),
	RemoveObjectFromCurrentLevel(NPC_0, identifier="EVENT_568_remove_from_current_level_2"),
	RemoveObjectFromCurrentLevel(NPC_2),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_4),
	JmpToEvent(E0261_FADE_MUSIC_ROOM_LOADER)
])
