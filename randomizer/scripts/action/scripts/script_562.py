#A0562_SONG_HINT_TADPOLE_SUMMONING

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetBit(TEMP_7043_6),
	ShiftToXYCoords(x=29, y=60),
	VisibilityOn(),
	SetSequenceSpeed(FAST),
	PlaySound(sound=SO050_WATER_DROPLET, channel=4),
	SetSpriteSequence(index=10, is_sequence=True, looping=True),
	Pause(12),
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	SetWalkingSpeed(FAST),
	ShiftSouthwestSteps(1),
	SetWalkingSpeed(NORMAL),
	ShiftSouthwestPixels(8),
	SetWalkingSpeed(SLOW),
	ShiftSouthwestPixels(5),
	Jmp(["ACTION_154_fixed_f_coord_on_0"])
])
