#A0762_STAR_HILL_2ND_ROOM_CENTRAL_SACKIT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShiftToXYCoords(x=17, y=55),
	ShadowOff(),
	FaceNortheast(),
	SetSequenceSpeed(VERY_FAST),
	SequenceLoopingOn(),
	VisibilityOn(),
	ShiftNortheastSteps(3),
	WalkToXYCoords(x=19, y=43),
	ShiftNorthwestSteps(20),
	ShiftSouthwestSteps(8),
	ShiftNorthwestSteps(4),
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
