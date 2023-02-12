# E2144_KEEP_2ND_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript([
	SetVarToConst(GAME_OVER_COUNTER_MAYBE, 2),
	FadeInFromBlack(sync=False),
	Return()
])
