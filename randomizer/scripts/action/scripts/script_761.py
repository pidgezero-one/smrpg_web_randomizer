#A0761_STAR_HILL_2ND_ROOM_WEST_SACKIT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShiftToXYCoords(x=3, y=51),
	ShadowOff(),
	FaceNortheast(),
	SetSequenceSpeed(VERY_FAST),
	SequenceLoopingOn(),
	VisibilityOn(),
	ShiftNortheastSteps(8),
	ShiftSoutheastSteps(4),
	ShiftNortheastSteps(12),
	ShiftNorthwestSteps(12),
	ShiftNortheastSteps(4),
	FaceNorthwest(),
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
