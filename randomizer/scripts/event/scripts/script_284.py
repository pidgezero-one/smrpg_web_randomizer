# E0284_OPEN_MUSHROOM_KINGDOM_SHOP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	OpenShop(SH00_MUSHROOM_KINGDOM),
	FadeInFromBlack(sync=False),
	Return()
])
