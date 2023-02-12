#A0716_BOOSTER_HILL_BUMP_FLOWER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	PlaySound(sound=SO085_FLOWER, channel=4),
	Db(bytearray(b'\x97\x1c')),
	SetVRAMPriority(PRIORITY_3),
	SetPriority(3),
	SetWalkingSpeed(FASTEST),
	AddZCoord1Step(),
	VisibilityOn(),
	SetWalkingSpeed(NORMAL),
	FloatingOff(),
	JumpToHeight(64),
	ShiftSoutheastPixels(12),
	FloatingOff(),
	SetWalkingSpeed(VERY_FAST),
	AddZCoord1Step(),
	StartLoopNTimes(8),
	VisibilityOn(),
	Pause(4),
	VisibilityOff(),
	Pause(1),
	EndLoop(),
	Return()
])
