# E2054_MONSTRO_MAIN_SHOP

from randomizer.scripts.event.script_imports import *

script = EventScript([
	OpenShop(SH17_MONSTRO),
	FadeInFromBlack(sync=False),
	Return()
])
