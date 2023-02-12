# E1171_SEASIDE_ACCESSORY_SHOP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	OpenShop(SH15_SEASIDE_ACCESSORY),
	FadeInFromBlack(sync=False),
	Return()
])
