# E0271_UNKNOWN

from randomizer.scripts.event.script_imports import *

script = EventScript([
	EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	FadeInFromBlack(sync=False),
	Return()
])
