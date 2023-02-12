# E1871_FIREWORKS_HOUSE_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	FadeOutMusicToVolume(duration=1, volume=96),
	JmpIfBitSet(MINECART_CLEARED, ["EVENT_1871_fade_in_from_black_async_3"]),
	RemoveObjectFromCurrentLevel(NPC_2),
	FadeInFromBlack(sync=False, identifier="EVENT_1871_fade_in_from_black_async_3"),
	Return()
])
