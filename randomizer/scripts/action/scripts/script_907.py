#A0907_MUSHROOM_THROWN_SOUTHWEST

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetSolidityBits(cant_pass_walls=True, cant_jump_through=True),
	SetVRAMPriority(PRIORITY_3),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
	JumpToHeight(height=48, silent=True),
	FloatingOn(),
	FaceSoutheast(),
	JmpIfBitSet(TEMP_7044_7, ["ACTION_907_set_object_memory_bits_9"]),
	FaceSouthwest(),
	SetObjectMemoryBits(arg_1=0x0B, bits=[0], identifier="ACTION_907_set_object_memory_bits_9"),
	Walk1StepFDirection(),
	SetSolidityBits(cant_pass_walls=True),
	Walk1StepFDirection(),
	SetVRAMPriority(NORMAL_PRIORITY),
	ShiftFDirectionSteps(6),
	StartLoopNTimes(7),
	VisibilityOn(),
	Pause(2),
	VisibilityOff(),
	Pause(2),
	EndLoop(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	VisibilityOff(),
	Return()
])
