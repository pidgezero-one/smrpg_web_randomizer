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
	ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	VisibilityOff(),
	FloatingOff(),
	TransferToObjectXY(NPC_0),
	TransferXYZFPixels(x=254, y=4, z=18, direction=SOUTHEAST),
	Pause(52),
	VisibilityOn(),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	FloatingOn(),
	SetSolidityBits(cant_pass_walls=True),
	SetVarToRandom(PRIMARY_TEMP_700C, 8),
	FaceEast7C(),
	JmpIfRandom1of2(["ACTION_933_jump_to_height_silent_23"]),
	JmpIfRandom1of2(["ACTION_933_jump_to_height_silent_19"]),
	JumpToHeight(height=128, silent=True),
	ShiftFDirectionSteps(4),
	SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	Jmp(["ACTION_727_jmp_if_var_equals_const_0"]),
	JumpToHeight(height=80, silent=True, identifier="ACTION_933_jump_to_height_silent_19"),
	ShiftFDirectionSteps(2),
	SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	Jmp(["ACTION_727_jmp_if_var_equals_const_0"]),
	JumpToHeight(height=160, silent=True, identifier="ACTION_933_jump_to_height_silent_23"),
	ShiftFDirectionSteps(6),
	SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	Jmp(["ACTION_727_jmp_if_var_equals_const_0"])
])
