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
	SetVRAMPriority(NORMAL),
	SetPriority(3),
	ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	FixedFCoordOff(),
	SetSolidityBits(cant_pass_walls=True),
	ObjectMemorySetBit(arg_1=0x09, bits=[7]),
	Db(bytearray(b'\xfd\x12')),
	SetAllSpeeds(speed=VERY_FAST),
	Set700CToPressedButton(),
	Mem700CAndConst(0x0003),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_471_transfer_to_xyzf_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_471_transfer_to_xyzf_21"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_471_transfer_to_xyzf_24"]),
	TransferToXYZF(x=18, y=46, z=0, direction=EAST),
	FaceNorthwest(),
	Jmp(["ACTION_471_visibility_on_26"]),
	TransferToXYZF(x=17, y=47, z=0, direction=EAST, identifier="ACTION_471_transfer_to_xyzf_18"),
	FaceNorthwest(),
	Jmp(["ACTION_471_visibility_on_26"]),
	TransferToXYZF(x=3, y=36, z=0, direction=EAST, identifier="ACTION_471_transfer_to_xyzf_21"),
	FaceNortheast(),
	Jmp(["ACTION_471_visibility_on_26"]),
	TransferToXYZF(x=3, y=37, z=0, direction=EAST, identifier="ACTION_471_transfer_to_xyzf_24"),
	FaceNortheast(),
	VisibilityOn(identifier="ACTION_471_visibility_on_26"),
	ShiftFDirectionSteps(15),
	Jmp(["ACTION_714_turn_clockwise_45_degrees_12"])
])
