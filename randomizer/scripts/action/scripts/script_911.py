#A0911_FROG_COIN_GETS_COLLECTED

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FloatingOff(),
	VisibilityOff(),
	Pause(9),
	SetSpriteSequence(index=2, is_sequence=True, looping=True),
	VisibilityOn(),
	ShiftZUpSteps(2),
	VisibilityOff(),
	Return()
])
