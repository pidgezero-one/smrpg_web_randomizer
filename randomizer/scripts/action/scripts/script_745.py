#A0745_STAR_HILL_1ST_ROOM_SOUTH_GECKO

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SequenceLoopingOn(identifier="ACTION_745_sequence_looping_on_0"),
	ShadowOff(),
	SetWalkingSpeed(VERY_SLOW),
	ShiftNortheastSteps(3),
	Pause(24),
	FaceSoutheast(),
	Pause(24),
	ShiftSoutheastSteps(4),
	ShiftSoutheastPixels(8),
	Pause(24),
	FaceSouthwest(),
	Pause(24),
	ShiftSouthwestSteps(8),
	Pause(24),
	FaceNorthwest(),
	Pause(24),
	ShiftNorthwestSteps(8),
	Pause(24),
	FaceNortheast(),
	Pause(24),
	ShiftNortheastSteps(3),
	ShiftNortheastPixels(4),
	Pause(24),
	FaceSoutheast(),
	Pause(24),
	ShiftSoutheastSteps(3),
	ShiftSoutheastPixels(8),
	Pause(24),
	FaceSoutheast(),
	Pause(24),
	WalkToXYCoords(x=10, y=107),
	Jmp(["ACTION_745_sequence_looping_on_0"])
])
