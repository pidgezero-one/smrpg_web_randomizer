# E2817_ASYNC_NO_ANIMATION_FLOWER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	PlaySound(sound=SO085_FLOWER, channel=6),
	SetVarToConst(PRIMARY_TEMP_7000, 1),
	Add7000ToMaxFP(),
	Return()
])
