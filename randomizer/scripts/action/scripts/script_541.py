#A0541_MIDDLE_GOOMBA_IN_MUSHROOM_WAY_2

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetBit(TEMP_7044_3),
	ClearSolidityBits(cant_pass_walls=True),
	SetAllSpeeds(VERY_FAST),
	ShiftSouthwestSteps(2),
	SetWalkingSpeed(FAST),
	SetSequenceSpeed(VERY_FAST),
	ShiftSouthwestSteps(6),
	SetWalkingSpeed(NORMAL),
	SetSequenceSpeed(FAST),
	ShiftSouthwestSteps(1),
	SetWalkingSpeed(SLOW),
	SetSequenceSpeed(NORMAL),
	ShiftSouthwestSteps(1),
	Pause(60),
	SetWalkingSpeed(NORMAL),
	SetSequenceSpeed(VERY_FAST),
	ShiftNortheastSteps(10),
	ClearBit(TEMP_7044_3),
	Return()
])
