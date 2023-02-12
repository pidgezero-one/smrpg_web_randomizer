#A0995_KEEP_BRIDGE_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(SLOW),
	ShiftSouthwestSteps(4, identifier="ACTION_995_shift_southwest_steps_2"),
	SetSequenceSpeed(VERY_FAST),
	SetWalkingSpeed(NORMAL),
	ShiftSouthwestSteps(3),
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(SLOW),
	ShiftSouthwestSteps(4),
	ShiftNorthwestSteps(1),
	ShiftNortheastSteps(4),
	SetSequenceSpeed(NORMAL),
	SetWalkingSpeed(VERY_SLOW),
	ShiftNortheastSteps(2),
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(SLOW),
	ShiftNortheastSteps(5),
	ShiftSoutheastSteps(1),
	Jmp(["ACTION_995_shift_southwest_steps_2"])
])
