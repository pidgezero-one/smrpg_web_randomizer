# E1125_SEASIDE_OCCUPIED_BOMB_SHOP_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0809_SEASIDE_OCCUPIED_BOMB_SHOP_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return()
])
