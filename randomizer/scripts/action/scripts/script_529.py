#A0529_MUSHROOM_WAY_1_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(SLOW),
	SetSequenceSpeed(FASTER),
	ShiftSouthwestSteps(1, identifier="ACTION_529_shift_southwest_steps_2"),
	ShiftSoutheastSteps(4),
	ShiftSouthwestSteps(6),
	ShiftNorthwestSteps(1),
	ShiftSouthwestSteps(3),
	ShiftNorthwestSteps(8),
	ShiftSouthwestSteps(1),
	ShiftNorthwestSteps(6),
	ShiftSouthwestSteps(2),
	ShiftNorthwestSteps(7),
	VisibilityOff(),
	ShiftToXYCoords(x=12, y=11),
	VisibilityOn(),
	ClearSolidityBits(cant_pass_walls=True),
	ShiftSouthwestSteps(4),
	ShiftSoutheastSteps(2),
	ShiftSouthwestSteps(1),
	ShiftSoutheastSteps(4),
	ShiftSouthwestSteps(1),
	ShiftSoutheastSteps(4),
	ShiftNortheastSteps(1),
	SetSolidityBits(cant_pass_walls=True),
	ShiftSoutheastSteps(6),
	Jmp(["ACTION_529_shift_southwest_steps_2"])
])
