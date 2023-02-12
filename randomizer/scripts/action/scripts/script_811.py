#A0811_NIMBUS_NPC_RANDOM_DIRECTIONS

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(VERY_SLOW),
	SetSequenceSpeed(SLOW),
	Db(bytearray(b' \x04')),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
	SetVarToConst(PRIMARY_TEMP_700C, 4, identifier="ACTION_811_set_11"),
	ShiftZ20Steps(),
	TurnClockwise45DegreesNTimes(6),
	Pause(4),
	TurnClockwise45DegreesNTimes(6),
	Pause(4),
	JmpIfRandom1of2(["ACTION_811_jmp_19"]),
	Pause(30),
	Jmp(["ACTION_811_set_11"], identifier="ACTION_811_jmp_19")
])
