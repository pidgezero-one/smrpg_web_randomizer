# E1123_SEASIDE_OCCUPIED_ELDERS_HOUSE_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0805_SEASIDE_OCCUPIED_ELDER_HOUSE_1F_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return()
])
