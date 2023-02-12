#A0982_DREAM_CUSHION_CHEF

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Pause(120),
	SetWalkingSpeed(SLOW),
	SetSequenceSpeed(FAST),
	ShiftSoutheastSteps(3, identifier="ACTION_982_shift_southeast_steps_3"),
	FaceNortheast(),
	Pause(60),
	ShiftNorthwestSteps(3),
	FaceNortheast(),
	Pause(60),
	Jmp(["ACTION_982_shift_southeast_steps_3"])
])
