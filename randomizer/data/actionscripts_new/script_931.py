#classes
from randomizer.types.actionscripts.commands import *
from randomizer.types.actionscripts.classes import ActionScript
#ids
from randomizer.types.eventscripts.constants.script_ids import *
from randomizer.types.actionscripts.constants.script_ids import *
from randomizer.types.packets.constants.packet_ids import *
from randomizer.types.constants.sound_names import *
from randomizer.types.constants.directions import *
#types
from randomizer.types.constants.area_objects import *
from randomizer.types.constants.coords import *
from randomizer.types.actionscripts.constants.sequence_speeds import *
from randomizer.types.actionscripts.constants.vram_priority import *
from randomizer.types.variables.variables import *

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
	SetSpriteSequence(index=0, is_sequence=True),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0]),
	Return(),
	TransferXYZFPixels(x=16, y=48, z=0, direction=EAST, identifier="ACTION_931_transfer_xyzf_pixels_12"),
	SetSpriteSequence(index=1, is_sequence=True),
	SetObjectMemoryBits(arg_1=0x0E, bits=[1]),
	Return(),
	SetVRAMPriority(NORMAL, identifier="ACTION_931_set_vram_priority_16"),
	TransferXYZFPixels(x=224, y=21, z=0, direction=EAST),
	SetSpriteSequence(index=2, is_sequence=True),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0, 1]),
	Return(),
	SetVRAMPriority(NORMAL, identifier="ACTION_931_set_vram_priority_21"),
	TransferXYZFPixels(x=224, y=53, z=0, direction=EAST),
	SetSpriteSequence(index=3, is_sequence=True),
	SetObjectMemoryBits(arg_1=0x0E, bits=[2]),
	Return(),
	SetVRAMPriority(NORMAL, identifier="ACTION_931_set_vram_priority_26"),
	TransferXYZFPixels(x=0, y=37, z=0, direction=EAST),
	SetSpriteSequence(index=4, is_sequence=True),
	SetObjectMemoryBits(arg_1=0x0E, bits=[0, 2]),
	Return()
])
