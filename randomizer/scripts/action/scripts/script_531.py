#A0531_MUSHROOM_WAY_1_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(SLOW),
	SetSequenceSpeed(FASTER),
	ShiftSouthwestSteps(2, identifier="ACTION_531_shift_southwest_steps_2"),
	ShiftNorthwestSteps(4),
	ShiftSouthwestSteps(1),
	ShiftNorthwestSteps(3),
	ShiftNortheastSteps(1),
	ShiftNorthwestSteps(1),
	VisibilityOff(),
	ShiftToXYCoords(x=12, y=11),
	VisibilityOn(),
	ShiftSouthwestSteps(3),
	ShiftSoutheastSteps(3),
	ShiftSouthwestSteps(4),
	ShiftSoutheastSteps(10),
	ShiftNortheastSteps(1),
	ShiftSoutheastSteps(6),
	ShiftSouthwestSteps(9),
	ShiftNorthwestSteps(6),
	ShiftSouthwestSteps(1),
	ShiftNorthwestSteps(7),
	Jmp(["ACTION_531_shift_southwest_steps_2"])
])
