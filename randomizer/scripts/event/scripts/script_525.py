# E0525_ROSE_TOWN_ITEM_SHOP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	OpenShop(SH01_ROSE_TOWN_ITEM),
	FadeInFromBlack(sync=False),
	Return()
])
