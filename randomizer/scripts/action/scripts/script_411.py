#A0411_FOREST_MAZE_AREA_BEE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(3),
	SetSequenceSpeed(NORMAL),
	SequenceLoopingOn(),
	Db(bytearray(b' \x07')),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x80\x00\x18\x00\x01\x00\x00\x00\x02\x80')),
	EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x80\x00\x10\x00\x01\x00\x00\x00\x02\x80")),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x80\x00\x10\x00\x01\x00\x00\x00\x04\x80')),
	Pause(1, identifier="ACTION_411_pause_7"),
	Jmp(["ACTION_411_pause_7"])
])
