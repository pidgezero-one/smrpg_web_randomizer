#A0168_BANDITS_WAY_3_CHOW

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(3, identifier="ACTION_168_set_priority_0"),
	FixedFCoordOn(),
	SequenceLoopingOn(identifier="ACTION_168_sequence_looping_on_2"),
	SetWalkingSpeed(VERY_SLOW),
	SetSequenceSpeed(VERY_FAST),
	ShiftNorthwestPixels(8),
	Pause(20),
	SetWalkingSpeed(FAST),
	SetSequenceSpeed(SLOW),
	JumpToHeight(height=36, silent=True),
	ShiftSoutheastPixels(8),
	Pause(25),
	Jmp(["ACTION_168_sequence_looping_on_2"])
])
