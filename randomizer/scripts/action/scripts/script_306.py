#A0306_WHIRLPOOL

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOff(),
	SetSequenceSpeed(VERY_SLOW),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 24, ["ACTION_306_jmp_to_subroutine_5"]),
	Pause(80),
	JmpToSubroutine(["ACTION_306_visibility_on_9"], identifier="ACTION_306_jmp_to_subroutine_5"),
	TransferXYZFSteps(x=0, y=0, z=10, direction=EAST),
	Pause(40),
	Jmp(["ACTION_306_jmp_to_subroutine_5"]),
	VisibilityOn(identifier="ACTION_306_visibility_on_9"),
	SetSpriteSequence(index=1, is_sequence=True, looping=True),
	Db(bytearray(b' \x03')),
	EmbeddedAnimationRoutine(bytearray(b'&\x00\x00\x00\x00\x00\x80\x00\x08\x00\x01\xf0\xff\x00\x10\x80')),
	EmbeddedAnimationRoutine(bytearray(b"\'\x00\x00\x00\x00\x00@\x00\x04\x00\x01\xf8\xff\x00\x10\x80")),
	ShiftZDownSteps(5),
	BPL262728(),
	VisibilityOff(),
	Return()
])
