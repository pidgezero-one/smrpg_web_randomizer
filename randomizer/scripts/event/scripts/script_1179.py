# E1179_JUICE_BAR_NO_CARD

from randomizer.scripts.event.script_imports import *

script = EventScript([
	OpenShop(SH09_JUICE_BAR_BASE),
	FadeInFromBlack(sync=False),
	Return()
])
