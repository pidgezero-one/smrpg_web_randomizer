#A0931_STUMPET

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_931_transfer_xyzf_pixels_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_931_transfer_xyzf_pixels_12"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_931_set_vram_priority_16"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 24, ["ACTION_931_set_vram_priority_21"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 25, ["ACTION_931_set_vram_priority_26"]),
	Return(),
	TransferXYZFPixels(x=16, y=16, z=0, direction=EAST, identifier="ACTION_931_transfer_xyzf_pixels_8"),
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
	Return(),
	TransferXYZFPixels(x=16, y=48, z=0, direction=EAST, identifier="ACTION_931_transfer_xyzf_pixels_12"),
	SetSpriteSequence(index=1, is_sequence=True, looping=True),
	SetObjectMemoryBits(arg_1=0x0E, bits=[1]),
	Return(),
	SetVRAMPriority(NORMAL_PRIORITY, identifier="ACTION_931_set_vram_priority_16"),
	TransferXYZFPixels(x=224, y=21, z=0, direction=EAST),
	SetSpriteSequence(index=2, is_sequence=True, looping=True),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1]),
	Return(),
	SetVRAMPriority(NORMAL_PRIORITY, identifier="ACTION_931_set_vram_priority_21"),
	TransferXYZFPixels(x=224, y=53, z=0, direction=EAST),
	SetSpriteSequence(index=3, is_sequence=True, looping=True),
	SetObjectMemoryBits(arg_1=0x0E, bits=[2]),
	Return(),
	SetVRAMPriority(NORMAL_PRIORITY, identifier="ACTION_931_set_vram_priority_26"),
	TransferXYZFPixels(x=0, y=37, z=0, direction=EAST),
	SetSpriteSequence(index=4, is_sequence=True, looping=True),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0, 2]),
	Return()
])
