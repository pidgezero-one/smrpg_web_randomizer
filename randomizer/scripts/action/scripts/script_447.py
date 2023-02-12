#A0447_LOOPING_SINGLE_SPARKLE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ObjectMemorySetBit(arg_1=0x3C, bits=[6]),
	ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	FloatingOff(),
	TransferToObjectXY(MARIO),
	JmpIfBitSet(EXP_STAR_BIT_5, ["ACTION_447_visibility_off_17"]),
	JmpIfBitSet(EXP_STAR_BIT_6, ["ACTION_447_visibility_off_17"]),
	JmpIfRandom1of2(["ACTION_447_shift_xy_pixels_9"]),
	ShiftXYPixels(x=4, y=4),
	Jmp(["ACTION_447_sequence_looping_on_10"]),
	ShiftXYPixels(x=252, y=252, identifier="ACTION_447_shift_xy_pixels_9"),
	SequenceLoopingOn(identifier="ACTION_447_sequence_looping_on_10"),
	SetSpriteSequence(index=1, is_sequence=True, looping=False),
	StartLoopNTimes(23),
	JmpIfBitSet(EXP_STAR_BIT_5, ["ACTION_447_visibility_off_17"]),
	JmpIfBitSet(EXP_STAR_BIT_6, ["ACTION_447_visibility_off_17"]),
	Pause(1),
	EndLoop(),
	VisibilityOff(identifier="ACTION_447_visibility_off_17"),
	Return()
])
