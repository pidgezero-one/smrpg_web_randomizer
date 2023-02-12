#A0759_STAR_HILL_2ND_ROOM_NORTH_SACKIT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShiftToXYCoords(x=25, y=7),
	ShadowOff(),
	FaceSouthwest(),
	SetSequenceSpeed(VERY_FAST),
	SequenceLoopingOn(),
	VisibilityOn(),
	ShiftSouthwestSteps(4),
	SetPriority(3),
	StartLoopNTimes(2),
	ShiftSoutheastSteps(4),
	ShiftSouthwestSteps(8),
	EndLoop(),
	Pause(8),
	ShadowOn(),
	JumpToHeight(128),
	SetWalkingSpeed(FASTER),
	ShiftSouthwestSteps(5),
	Pause(56),
	SetWalkingSpeed(VERY_FAST),
	SetSequenceSpeed(FASTEST),
	ShiftSouthwestSteps(32),
	VisibilityOff(),
	Return()
])
