#A0525_SPINNING_CARD

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FloatingOff(),
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	VisibilityOff(),
	Pause(9),
	VisibilityOn(),
	Pause(24),
	VisibilityOff(),
	Return()
])
