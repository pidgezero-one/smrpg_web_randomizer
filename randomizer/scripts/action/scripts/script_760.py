#A0760_STAR_HILL_2ND_ROOM_EAST_SACKIT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShiftToXYCoords(x=29, y=55),
	ShadowOff(),
	FaceNorthwest(),
	SetSequenceSpeed(VERY_FAST),
	SequenceLoopingOn(),
	VisibilityOn(),
	ShiftNorthwestSteps(12),
	ShiftNortheastSteps(8),
	ShiftNorthwestSteps(12),
	SetPriority(3),
	ShiftNortheastSteps(12),
	Pause(8),
	ShadowOn(),
	JumpToHeight(128),
	SetWalkingSpeed(FASTER),
	ShiftNortheastSteps(5),
	Pause(56),
	SetWalkingSpeed(VERY_FAST),
	SetSequenceSpeed(FASTEST),
	ShiftNortheastSteps(8),
	VisibilityOff(),
	Return()
])
