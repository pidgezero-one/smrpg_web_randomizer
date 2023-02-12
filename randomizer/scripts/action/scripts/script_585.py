#A0585_SEASIDE_OCCUPIED_SHOPKEEPER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceSoutheast(),
	FixedFCoordOn(),
	SequenceLoopingOn(),
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(VERY_SLOW),
	ShiftSouthwestSteps(2, identifier="ACTION_585_shift_southwest_steps_5"),
	ShiftNortheastSteps(3),
	ShiftSouthwestSteps(1),
	Jmp(["ACTION_585_shift_southwest_steps_5"])
])
