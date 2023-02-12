#A0749_STAR_HILL_1ST_ROOM_SOUTHEAST_SACKIT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShiftToXYCoords(x=4, y=103),
	ShadowOff(),
	FaceSoutheast(),
	SetSequenceSpeed(VERY_FAST),
	SequenceLoopingOn(),
	VisibilityOn(),
	ShiftSoutheastSteps(8),
	Pause(8),
	ShiftNortheastSteps(8),
	SetPriority(3),
	ShiftSoutheastSteps(4),
	Pause(8),
	ShiftSouthwestSteps(16),
	Pause(8),
	ShadowOn(),
	JumpToHeight(128),
	SetWalkingSpeed(FASTER),
	ShiftSouthwestSteps(5),
	Pause(64),
	SetWalkingSpeed(VERY_FAST),
	SetSequenceSpeed(FASTEST),
	ShiftSouthwestSteps(8),
	VisibilityOff(),
	Return()
])
