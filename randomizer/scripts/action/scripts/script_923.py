#A0923_SHIP_STAIRCASE_ZEOSTARS

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
	ShadowOff(),
	Set700CToPressedButton(),
	Mem700CAndConst(0x0003),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_923_db_10"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_923_pause_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_923_pause_8"]),
	Pause(15),
	Pause(15, identifier="ACTION_923_pause_8"),
	Pause(15, identifier="ACTION_923_pause_9"),
	Db(bytearray(b' \x05'), identifier="ACTION_923_db_10"),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00\x08\x00\x01\x00\x00\x00\x01\x80')),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\xc0\x00\x02\x00\x01\x00\x00\x00\x02\x80')),
	Pause(1, identifier="ACTION_923_pause_13"),
	Jmp(["ACTION_923_pause_13"])
])
