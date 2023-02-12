# E2819_ASYNC_NO_ANIMATION_1_COIN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	PlaySound(sound=SO013_COIN, channel=6),
	SetVarToConst(PRIMARY_TEMP_7000, 1),
	AddCoins(PRIMARY_TEMP_7000),
	Return()
])
