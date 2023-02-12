#A0530_MUSHROOM_WAY_1_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(SLOW),
	SetSequenceSpeed(FASTER),
	ShiftNorthwestSteps(10, identifier="ACTION_530_shift_northwest_steps_2"),
	ShiftSouthwestSteps(2),
	ShiftNorthwestSteps(6),
	ShiftSouthwestSteps(1),
	ShiftNorthwestSteps(5),
	VisibilityOff(),
	ShiftToXYCoords(x=12, y=11),
	VisibilityOn(),
	ShiftSouthwestSteps(4),
	ShiftSoutheastSteps(6),
	ShiftSouthwestSteps(3),
	ShiftSoutheastSteps(8),
	ShiftNortheastSteps(1),
	ShiftSoutheastSteps(4),
	ShiftSouthwestSteps(1),
	ShiftSoutheastSteps(1),
	ShiftSouthwestSteps(1),
	ShiftSoutheastSteps(1),
	ShiftSouthwestSteps(5),
	ShiftNorthwestSteps(1),
	ShiftSouthwestSteps(2),
	Jmp(["ACTION_530_shift_northwest_steps_2"])
])
