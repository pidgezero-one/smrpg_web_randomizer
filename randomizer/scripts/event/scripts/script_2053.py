# E2053_MONSTRO_GOOMBETTE_SHOP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	OpenShop(SH20_GOOMBETTE),
	FadeInFromBlack(sync=False),
	Return()
])
