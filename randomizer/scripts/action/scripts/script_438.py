#A0438_ROSE_WAY_SWINGING_PLATFORM_2

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ObjectMemorySetBit(arg_1=0x0D, bits=[6]),
	SetPriority(3),
	Db(bytearray(b' \x07')),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00@\x00\x01\x00\x00\x00\x02\x80')),
	EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x00\x00 \x00\x01\x00\x00\x00\x02\x80")),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\xc0\x00\x0c\x00\x01\x00\x00\x00\x04\x80')),
	Pause(1, identifier="ACTION_438_pause_6"),
	Jmp(["ACTION_438_pause_6"])
])
