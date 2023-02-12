# E1173_SEASIDE_WEAPON_SHOP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	OpenShop(SH13_SEASIDE_WEAPON),
	FadeInFromBlack(sync=False),
	Return()
])
