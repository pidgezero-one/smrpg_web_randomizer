#A0993_KEEP_BRIDGE_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(SLOW),
	ShiftNortheastSteps(5, identifier="ACTION_993_shift_northeast_steps_2"),
	FaceSouthwest(),
	FixedFCoordOn(),
	SetSequenceSpeed(NORMAL),
	SetWalkingSpeed(VERY_SLOW),
	ShiftNortheastSteps(2),
	FixedFCoordOff(),
	FaceNortheast(),
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(SLOW),
	ShiftNortheastSteps(3),
	SetSequenceSpeed(VERY_FAST),
	SetWalkingSpeed(NORMAL),
	ShiftNortheastSteps(1),
	ShiftSoutheastSteps(1),
	ShiftSouthwestSteps(1),
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(SLOW),
	ShiftSouthwestSteps(10),
	ShiftNorthwestSteps(1),
	Jmp(["ACTION_993_shift_northeast_steps_2"])
])
