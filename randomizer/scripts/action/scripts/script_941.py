#A0941_VOLCANO_1ST_BOSS

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SequenceLoopingOn(),
	VisibilityOff(),
	SetPriority(3),
	Db(bytearray(b' \x04')),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x00\x08\x00\x01\x00\x00\x00\x02\x80')),
	Pause(500),
	StartLoopNTimes(9),
	VisibilityOn(),
	Pause(4),
	VisibilityOff(),
	Pause(4),
	EndLoop(),
	PlaySound(sound=SO119_CZAR_DRAGON_ROAR, channel=4),
	StartLoopNTimes(9),
	VisibilityOn(),
	Pause(2),
	VisibilityOff(),
	Pause(2),
	EndLoop(),
	StartLoopNTimes(9),
	VisibilityOn(),
	Pause(1),
	VisibilityOff(),
	Pause(1),
	EndLoop(),
	VisibilityOn(),
	Jmp(["ACTION_936_pause_16"])
])
