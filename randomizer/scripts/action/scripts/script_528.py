#A0528_MUSHROOM_WAY_1_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(SLOW),
	SetSequenceSpeed(FASTER),
	ShiftSouthwestSteps(1, identifier="ACTION_528_shift_southwest_steps_2"),
	ShiftSoutheastSteps(12),
	ShiftSouthwestSteps(3),
	ShiftSoutheastSteps(1),
	ShiftSouthwestSteps(4),
	ShiftNorthwestSteps(1),
	ShiftSouthwestSteps(2),
	ShiftNorthwestSteps(6),
	ShiftSouthwestSteps(1),
	ShiftNorthwestSteps(7),
	ShiftSouthwestSteps(2),
	ShiftNorthwestSteps(8),
	VisibilityOff(),
	ShiftToXYCoords(x=12, y=11),
	VisibilityOn(),
	ShiftSouthwestSteps(2),
	ShiftSoutheastSteps(1),
	ShiftSouthwestSteps(1),
	ShiftSoutheastSteps(1),
	ShiftSouthwestSteps(1),
	ShiftSoutheastSteps(3),
	ShiftSouthwestSteps(1),
	ShiftSoutheastSteps(2),
	Jmp(["ACTION_528_shift_southwest_steps_2"])
])
