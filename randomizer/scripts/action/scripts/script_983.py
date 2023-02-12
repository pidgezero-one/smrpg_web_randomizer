#A0983_DREAM_CUSHION_CHEF

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Pause(90),
	SetWalkingSpeed(SLOW),
	SetSequenceSpeed(FAST),
	ShiftSouthwestSteps(3, identifier="ACTION_983_shift_southwest_steps_3"),
	Pause(30),
	SetSequenceSpeed(NORMAL),
	SetSpriteSequence(index=3, is_sequence=True, looping=True),
	Pause(40),
	ResetProperties(),
	SetSequenceSpeed(FAST),
	ShiftNortheastSteps(3),
	Pause(90),
	Jmp(["ACTION_983_shift_southwest_steps_3"])
])
