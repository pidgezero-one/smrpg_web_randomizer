#A0603_MIDAS_1ST_TUNNEL_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(3),
	Db(bytearray(b' \x03')),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\xc0\x00 \x00\x01\x00\x00\x00\x01\x80')),
	EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x00\x00\x10\x00\x01\x00\x00\x00\x01\x80")),
	TurnClockwise45DegreesNTimes(2, identifier="ACTION_603_turn_clockwise_45_degrees_n_times_4"),
	Pause(7),
	Jmp(["ACTION_603_turn_clockwise_45_degrees_n_times_4"])
])
