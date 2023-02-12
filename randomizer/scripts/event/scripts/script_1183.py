# E1183_VOLCANO_ITEM_SHOP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	OpenShop(SH18_VOLCANO_ITEM),
	FadeInFromBlack(sync=False),
	Return()
])
