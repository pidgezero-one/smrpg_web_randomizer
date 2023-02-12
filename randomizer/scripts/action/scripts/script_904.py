#A0904_COIN_GETS_COLLECTED

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShadowOff(),
	SetVRAMPriority(PRIORITY_3),
	SetSpriteSequence(index=2, is_sequence=True, looping=True),
	ShiftZUpSteps(2),
	VisibilityOff(),
	Return()
])
