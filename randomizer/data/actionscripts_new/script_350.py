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
	VisibilityOff(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	SetAllSpeeds(speed=FAST),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	Set700CToPressedButton(),
	Mem700CAndConst(0x0007),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_350_create_packet_at_npc_coords_20"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_350_pause_19"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_350_pause_18"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_350_pause_17"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_350_pause_16"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_350_pause_15"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["ACTION_350_pause_14"]),
	Pause(20),
	Pause(20, identifier="ACTION_350_pause_14"),
	Pause(20, identifier="ACTION_350_pause_15"),
	Pause(20, identifier="ACTION_350_pause_16"),
	Pause(20, identifier="ACTION_350_pause_17"),
	Pause(20, identifier="ACTION_350_pause_18"),
	Pause(20, identifier="ACTION_350_pause_19"),
	CreatePacketAtNPCCoords(packet_id=P024_REGULAR_SOUND_EXPLOSION, object=DUMMY_0X07, destinations=["ACTION_350_visibility_on_21"], identifier="ACTION_350_create_packet_at_npc_coords_20"),
	VisibilityOn(identifier="ACTION_350_visibility_on_21"),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	StartLoopNTimes(7),
	Walk1StepFDirection(),
	ShadowOn(),
	EndLoop(),
	VisibilityOff(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	Pause(128),
	Set700CToPressedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 26, ["ACTION_350_transfer_to_xyzf_39"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 27, ["ACTION_350_transfer_to_xyzf_41"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 28, ["ACTION_350_transfer_to_xyzf_43"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 29, ["ACTION_350_transfer_to_xyzf_45"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 30, ["ACTION_350_transfer_to_xyzf_47"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 31, ["ACTION_350_transfer_to_xyzf_49"]),
	TransferToXYZF(x=23, y=59, z=10, direction=EAST, identifier="ACTION_350_transfer_to_xyzf_39"),
	Jmp(["ACTION_350_create_packet_at_npc_coords_20"]),
	TransferToXYZF(x=21, y=63, z=10, direction=EAST, identifier="ACTION_350_transfer_to_xyzf_41"),
	Jmp(["ACTION_350_create_packet_at_npc_coords_20"]),
	TransferToXYZF(x=30, y=63, z=10, direction=EAST, identifier="ACTION_350_transfer_to_xyzf_43"),
	Jmp(["ACTION_350_create_packet_at_npc_coords_20"]),
	TransferToXYZF(x=28, y=59, z=10, direction=EAST, identifier="ACTION_350_transfer_to_xyzf_45"),
	Jmp(["ACTION_350_create_packet_at_npc_coords_20"]),
	TransferToXYZF(x=22, y=61, z=10, direction=EAST, identifier="ACTION_350_transfer_to_xyzf_47"),
	Jmp(["ACTION_350_create_packet_at_npc_coords_20"]),
	TransferToXYZF(x=29, y=61, z=10, direction=EAST, identifier="ACTION_350_transfer_to_xyzf_49"),
	Jmp(["ACTION_350_create_packet_at_npc_coords_20"])
])
