#A0064_KINGDOM_FAST_KID

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(VERY_FAST),
	SetWalkingSpeed(VERY_FAST),
	ShiftNortheastSteps(1, identifier="ACTION_64_shift_northeast_steps_2"),
	ShiftSoutheastSteps(3),
	ShiftSouthwestSteps(4),
	ShiftNorthwestSteps(3),
	ShiftNortheastSteps(3),
	Jmp(["ACTION_64_shift_northeast_steps_2"])
])
