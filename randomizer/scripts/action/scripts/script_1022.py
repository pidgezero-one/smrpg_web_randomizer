#A1022_HIT_BY_EXP_STAR

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	PlaySound(sound=SO066_KICK_BALL_SHELL, channel=4),
	Db(bytearray(b'\xfd\xf2')),
	SetVRAMPriority(PRIORITY_3),
	SetPriority(3),
	OverwriteSolidity(),
	ObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
	FloatingOff(),
	FixedFCoordOn(),
	Db(bytearray(b' \x07')),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x00\x00')),
	EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00\x00\x00\x05\x00\x01\x00\x00\x00\x00\x00")),
	Db(bytearray(b'\xfd$\x00\x07')),
	JmpIfRandom1of2(["ACTION_1022_db_17"]),
	JmpIfRandom1of2(["ACTION_1022_add_16"]),
	AddConstToVar(PRIMARY_TEMP_700C, 24),
	Jmp(["ACTION_1022_db_17"]),
	AddConstToVar(PRIMARY_TEMP_700C, 232, identifier="ACTION_1022_add_16"),
	Db(bytearray(b'\xfd%'), identifier="ACTION_1022_db_17"),
	Db(bytearray(b'%\xa0\x08\x80\xff')),
	Pause(64),
	BPL262728(),
	VisibilityOff(),
	EndAll()
])
