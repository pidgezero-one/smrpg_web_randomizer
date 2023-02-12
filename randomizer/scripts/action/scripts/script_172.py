#A0172_ENDING_CUTSCENE_SPARKLES

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FixedFCoordOn(),
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	LoadMemory(TEMP_702E),
	Pause(1),
	JmpIfMarioInAir(["ACTION_172_ret_28"]),
	EndLoop(),
	StartLoopNTimes(11),
	SetWalkingSpeed(FAST),
	ShiftZDownPixels(2),
	ShiftZUpPixels(2),
	JmpIfMarioInAir(["ACTION_172_ret_28"]),
	EndLoop(),
	JumpToHeight(height=0, silent=True),
	FloatingOn(),
	Pause(1, identifier="ACTION_172_pause_14"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_172_pause_14"]),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	VisibilityOff(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	ShiftZUpSteps(9),
	StartLoopNTimes(4),
	Pause(1),
	VisibilityOff(),
	Pause(1),
	VisibilityOn(),
	EndLoop(),
	SetSolidityBits(cant_walk_through=True),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	Return(identifier="ACTION_172_ret_28")
])
