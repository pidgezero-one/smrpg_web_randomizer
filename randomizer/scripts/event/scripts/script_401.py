# E0401_GUEST_ROOM_ANTECHAMBER_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	JmpIfBitClear(MUSHROOM_KINGDOM_LIBERATED, ["EVENT_401_fade_in_from_black_async_9"]),
	SummonObjectToCurrentLevel(NPC_0),
	FadeInFromBlack(sync=False, identifier="EVENT_401_fade_in_from_black_async_9"),
	Return()
])
