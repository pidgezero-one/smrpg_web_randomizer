#A0810_NIMBUS_NPC_RANDOM_DIRECTIONS

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(VERY_SLOW),
	SetSequenceSpeed(SLOW),
	Db(bytearray(b' \x04')),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00@\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
	SetVarToConst(PRIMARY_TEMP_700C, 2, identifier="ACTION_810_set_13"),
	ShiftZ20Steps(),
	TurnClockwise45DegreesNTimes(6),
	Pause(4),
	TurnClockwise45DegreesNTimes(6),
	Pause(4),
	TurnClockwise45DegreesNTimes(6),
	JmpIfRandom1of2(["ACTION_810_jmp_22"]),
	Pause(15),
	Jmp(["ACTION_810_set_13"], identifier="ACTION_810_jmp_22")
])
