# E1856_MOLEVILLE_SHOP_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SummonObjectToCurrentLevel(NPC_0),
	FadeOutMusicToVolume(duration=1, volume=96),
	JmpIfBitSet(MINECART_CLEARED, ["EVENT_1856_jmp_to_event_5"]),
	RemoveObjectFromCurrentLevel(NPC_1),
	RemoveObjectFromCurrentLevel(NPC_3),
	RemoveObjectFromCurrentLevel(NPC_5),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1856_jmp_to_event_5")
])
