#A0241_SMITHY_COMPONENT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Pause(5),
	SequenceLoopingOn(),
	SetAllSpeeds(FAST),
	ShiftSouthwestPixels(2),
	SetWalkingSpeed(NORMAL),
	ShiftNortheastPixels(2),
	SetWalkingSpeed(SLOW),
	ShiftNortheastPixels(1),
	SetSequenceSpeed(SLOW),
	SetWalkingSpeed(NORMAL),
	ShiftNorthPixels(2),
	SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
	Pause(15),
	ShiftSouthwestPixels(1),
	SetWalkingSpeed(FAST),
	ShiftSouthPixels(2),
	Pause(7),
	SetSequenceSpeed(NORMAL),
	SetSpriteSequence(index=1, is_sequence=True, looping=True),
	Return()
])
