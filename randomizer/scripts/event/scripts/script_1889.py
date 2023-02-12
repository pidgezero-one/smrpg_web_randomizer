# E1889_ABYSS_SIDE_TREASURE_ROOMS_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	ClearBit(UNKNOWN_DIRECTIONAL_BIT_1),
	ClearBit(ABYSS_TWO_CHEST_ROOM_DIRECTIONAL_BIT),
	FadeInFromBlack(sync=False),
	Return()
])
