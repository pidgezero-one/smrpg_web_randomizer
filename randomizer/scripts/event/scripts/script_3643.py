# E3643_NIMBUS_SHOP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	OpenShop(SH21_NIMBUS_LAND),
	FadeInFromBlack(sync=False),
	Return()
])
