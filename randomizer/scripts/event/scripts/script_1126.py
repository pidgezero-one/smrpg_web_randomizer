# E1126_SEASIDE_OCCUPIED_ARMOR_SHOP_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	RunEventAsSubroutine(E0810_SEASIDE_OCCUPIED_WPN_ARM_SHOP_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	Return()
])
