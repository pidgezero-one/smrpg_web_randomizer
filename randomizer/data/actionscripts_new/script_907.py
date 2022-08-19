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
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetSolidityBits(cant_pass_walls=True, cant_jump_through=True),
	SetVRAMPriority(PRIORITY_3),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True),
	JumpToHeight(height=48, silent=True),
	FloatingOn(),
	FaceSoutheast(),
	JmpIfBitSet(TEMP_7044_7, ["ACTION_907_set_object_memory_bits_9"]),
	FaceSouthwest(),
	SetObjectMemoryBits(arg_1=0x0B, bits=[0], identifier="ACTION_907_set_object_memory_bits_9"),
	Walk1StepFDirection(),
	SetSolidityBits(cant_pass_walls=True),
	Walk1StepFDirection(),
	SetVRAMPriority(NORMAL),
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
