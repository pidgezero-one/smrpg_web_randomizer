#A0913_KEY_APPEARS_BRIEFLY

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FloatingOff(),
	SetSpriteSequence(index=2, is_sequence=True, looping=True),
	VisibilityOff(),
	Pause(9),
	VisibilityOn(),
	Pause(24),
	VisibilityOff(),
	Return()
])
