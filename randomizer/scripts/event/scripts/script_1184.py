# E1184_VOLCANO_ARMOR_SHOP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	OpenShop(SH19_VOLCANO_ARMOR),
	FadeInFromBlack(sync=False),
	Return()
])
