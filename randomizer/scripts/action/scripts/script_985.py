#A0985_DREAM_CUSHION_CHEF

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Pause(90, identifier="ACTION_985_pause_0"),
	SetSpriteSequence(index=2, is_sequence=True, looping=True),
	Pause(48),
	ResetProperties(),
	SetSequenceSpeed(FAST),
	ShiftNortheastSteps(3),
	SetBit(TEMP_7043_1),
	Pause(10),
	ClearBit(TEMP_7043_1),
	Pause(30),
	ShiftSouthwestSteps(3),
	SetSequenceSpeed(NORMAL),
	Jmp(["ACTION_985_pause_0"])
])
