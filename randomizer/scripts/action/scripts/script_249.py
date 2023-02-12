#A0249_WATER_BLAST_SFX

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	Pause(20),
	PlaySound(sound=SO146_MACHINE_TRANSFORM, channel=4),
	Pause(20),
	VisibilityOff(),
	SetBit(TEMP_7043_7),
	Return()
])
