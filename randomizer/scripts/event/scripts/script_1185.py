# E1185_TOAD_SHOP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	OpenShop(SH24_FACTORY_TOAD),
	FadeInFromBlack(sync=False),
	Return()
])
