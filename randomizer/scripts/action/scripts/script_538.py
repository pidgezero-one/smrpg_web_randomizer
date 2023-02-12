#A0538_RIGHT_GOOMBA_IN_MUSHROOM_WAY_2

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetBit(TEMP_7044_5),
	ClearSolidityBits(cant_pass_walls=True),
	SetWalkingSpeed(FAST),
	SetSequenceSpeed(VERY_FAST),
	ShiftSoutheastSteps(7),
	SetWalkingSpeed(NORMAL),
	SetSequenceSpeed(FAST),
	ShiftSoutheastSteps(1),
	SetWalkingSpeed(SLOW),
	SetSequenceSpeed(NORMAL),
	ShiftSoutheastSteps(1),
	Pause(60),
	SetWalkingSpeed(NORMAL),
	SetSequenceSpeed(VERY_FAST),
	ShiftNorthwestSteps(9),
	Pause(5),
	ClearBit(TEMP_7044_5),
	Return()
])
