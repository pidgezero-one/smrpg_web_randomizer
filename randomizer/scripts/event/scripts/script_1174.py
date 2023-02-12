# E1174_SEASIDE_ARMOR_SHOP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	OpenShop(SH14_SEASIDE_ARMOR),
	FadeInFromBlack(sync=False),
	Return()
])
