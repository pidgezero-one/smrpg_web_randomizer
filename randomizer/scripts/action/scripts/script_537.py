#A0537_LEFT_GOOMBA_IN_MUSHROOM_WAY_2

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetBit(TEMP_7044_6),
	FaceSoutheast(),
	FixedFCoordOn(),
	SetWalkingSpeed(FAST),
	SetSequenceSpeed(VERY_FAST),
	ShiftSouthwestSteps(1),
	Pause(25),
	FixedFCoordOff(),
	ShiftSoutheastSteps(9),
	SetWalkingSpeed(NORMAL),
	SetSequenceSpeed(FAST),
	ShiftSoutheastSteps(1),
	SetWalkingSpeed(SLOW),
	SetSequenceSpeed(NORMAL),
	ShiftSoutheastSteps(1),
	Pause(60),
	SetWalkingSpeed(NORMAL),
	SetSequenceSpeed(VERY_FAST),
	ShiftNorthwestSteps(11),
	ShiftNortheastSteps(1),
	ClearBit(TEMP_7044_6),
	Return()
])
