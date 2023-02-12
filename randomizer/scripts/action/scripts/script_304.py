#A0304_OUTER_SEA_WHIRLPOOL

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOff(),
	SetSequenceSpeed(VERY_SLOW),
	Set700CToPressedButton(),
	Mem700CAndConst(0x0006),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_304_pause_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_304_pause_9"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_304_pause_10"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["ACTION_304_jmp_to_subroutine_11"]),
	Pause(80, identifier="ACTION_304_pause_8"),
	Pause(80, identifier="ACTION_304_pause_9"),
	Pause(80, identifier="ACTION_304_pause_10"),
	JmpToSubroutine(["ACTION_304_visibility_on_21"], identifier="ACTION_304_jmp_to_subroutine_11"),
	TransferXYZFSteps(x=2, y=4, z=20, direction=NORTHEAST),
	Pause(40),
	JmpToSubroutine(["ACTION_304_visibility_on_21"]),
	TransferXYZFSteps(x=253, y=254, z=20, direction=NORTHEAST),
	Pause(40),
	JmpToSubroutine(["ACTION_304_visibility_on_21"]),
	TransferXYZFSteps(x=1, y=254, z=20, direction=NORTHEAST),
	Pause(40),
	Jmp(["ACTION_304_jmp_to_subroutine_11"]),
	VisibilityOn(identifier="ACTION_304_visibility_on_21"),
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	Db(bytearray(b' \x03')),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x08\x00\x00\x10\x80')),
	EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00@\x00\x00\x00\x01\x04\x00\x00\x10\x80")),
	ShiftZUpSteps(6),
	BPL262728(),
	VisibilityOff(),
	Return()
])
