#A0747_STAR_HILL_1ST_ROOM_NORTH_SACKIT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShiftToXYCoords(x=2, y=84),
	ShadowOff(),
	FaceSoutheast(),
	SetSequenceSpeed(VERY_FAST),
	SequenceLoopingOn(),
	VisibilityOn(),
	StartLoopNTimes(2),
	ShiftSoutheastSteps(4),
	ShiftNortheastSteps(4),
	EndLoop(),
	ShiftSoutheastSteps(2),
	Pause(8),
	ShadowOn(),
	JumpToHeight(128),
	SetWalkingSpeed(FASTER),
	ShiftSoutheastSteps(5),
	Pause(64),
	SetWalkingSpeed(VERY_FAST),
	SetSequenceSpeed(FASTEST),
	ShiftSoutheastSteps(10),
	VisibilityOff(),
	Return()
])
