#A0238_CHEERING_NIMBITES

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSpriteSequence(index=6, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	SetWalkingSpeed(SLOW),
	ShiftZUpPixels(4),
	Pause(4),
	ShiftZDownPixels(4),
	ResetProperties(),
	Return()
])
