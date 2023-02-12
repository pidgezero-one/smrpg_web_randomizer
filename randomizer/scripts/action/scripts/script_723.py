#A0723_MINES_RECRUITABLE_CHARACTER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceSouthwest(),
	FixedFCoordOn(),
	SequencePlaybackOn(),
	SequenceLoopingOn(),
	ShiftNortheastPixels(3),
	FaceSouthwest(identifier="ACTION_723_face_southwest_5"),
	FixedFCoordOn(),
	StartLoopNTimes(3),
	ShiftWestPixels(1),
	Pause(1),
	ShiftEastPixels(1),
	Pause(1),
	EndLoop(),
	SetWalkingSpeed(SLOW),
	ShiftNortheastPixels(8),
	Pause(80),
	JmpIfRandom1of2(["ACTION_723_face_southwest_23"]),
	FixedFCoordOff(),
	FaceNorthwest(),
	JumpToHeight(40),
	Pause(16),
	JumpToHeight(40),
	Pause(64),
	FaceSouthwest(identifier="ACTION_723_face_southwest_23"),
	FixedFCoordOn(),
	ShiftSouthwestPixels(8),
	SetWalkingSpeed(NORMAL),
	Jmp(["ACTION_723_face_southwest_5"])
])
