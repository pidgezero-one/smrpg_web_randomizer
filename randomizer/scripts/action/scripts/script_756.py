#A0756_STAR_HILL_3RD_ROOM_SACKIT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShiftToXYCoords(x=28, y=121),
	ShadowOff(),
	FaceNorthwest(),
	SetSequenceSpeed(VERY_FAST),
	SequenceLoopingOn(),
	VisibilityOn(),
	ShiftNorthwestSteps(8),
	ShiftSouthwestSteps(4),
	ShiftNorthwestSteps(8),
	Pause(8),
	ShadowOn(),
	JumpToHeight(128),
	SetWalkingSpeed(FASTER),
	ShiftNorthwestSteps(5),
	Pause(56),
	SetWalkingSpeed(VERY_FAST),
	SetSequenceSpeed(FASTEST),
	ShiftNorthwestSteps(8),
	VisibilityOff(),
	Return()
])
