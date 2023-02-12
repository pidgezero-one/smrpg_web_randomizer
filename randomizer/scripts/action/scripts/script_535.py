#A0535_MUSHROOM_WAY_2_RECRUITABLE_CHARACTER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Db(bytearray(b' \x04'), identifier="ACTION_535_db_0"),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(SLOW),
	ShiftSoutheastSteps(2),
	ShiftNortheastSteps(2),
	ShiftNorthwestSteps(2),
	ShiftSouthwestSteps(2),
	Jmp(["ACTION_535_db_0"])
])
