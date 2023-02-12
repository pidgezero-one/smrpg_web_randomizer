# E1180_JUICE_BAR_ALTO_CARD

from randomizer.scripts.event.script_imports import *

script = EventScript([
	OpenShop(SH10_JUICE_BAR_ALTO),
	FadeInFromBlack(sync=False),
	Return()
])
