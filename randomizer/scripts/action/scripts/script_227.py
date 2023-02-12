#A0227_ENDING_CUTSCENE_EFFECT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(VERY_SLOW),
	SetSpriteSequence(index=10, sprite_offset=2, is_sequence=True, looping=True),
	Pause(98),
	SetSequenceSpeed(SLOW),
	Pause(162),
	SetSequenceSpeed(NORMAL),
	Pause(162),
	SetSequenceSpeed(FAST),
	Pause(214),
	SetSequenceSpeed(FASTER),
	Pause(216),
	SetSequenceSpeed(VERY_FAST),
	Pause(384),
	SetWalkingSpeed(VERY_SLOW),
	AddZCoord1Step(),
	Return()
])
