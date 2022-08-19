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
	Set700CToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 13, ["ACTION_942_set_700C_to_pressed_button_37"]),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	VisibilityOff(),
	ClearSolidityBits(cant_pass_walls=True),
	ShiftSoutheastPixels(7),
	ShiftNortheastPixels(3),
	SetObjectMemoryBits(arg_1=0x0B),
	Walk1StepNortheast(),
	Db(bytearray(b'\xc8\x07')),
	CopyVarToVar(from_var=X_COORD_2, to_var=SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=Y_COORD_2, to_var=TEMP_7026),
	Pause(100, identifier="ACTION_942_pause_13"),
	VisibilityOn(),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	Walk1StepSouthwest(),
	SetSolidityBits(cant_pass_walls=True),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SequenceLoopingOn(),
	FixedFCoordOff(),
	StartLoopNTimes(254),
	FaceMario(),
	Pause(4),
	EndLoop(),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	SetObjectMemoryBits(arg_1=0x0B, bits=[0]),
	ClearSolidityBits(cant_pass_walls=True),
	Walk1StepNortheast(),
	VisibilityOff(),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=X_COORD_2),
	CopyVarToVar(from_var=TEMP_7026, to_var=Y_COORD_2),
	TransferTo70167018(),
	Pause(900),
	Jmp(["ACTION_942_pause_13"]),
	Set700CToPressedButton(identifier="ACTION_942_set_700C_to_pressed_button_37"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 21, ["ACTION_942_db_43"]),
	Db(bytearray(b' \x04')),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x00\x03\x00\x01\x00\x00\x00\x03\x80')),
	Pause(1, identifier="ACTION_942_pause_41"),
	Jmp(["ACTION_942_pause_41"]),
	Db(bytearray(b' \x04'), identifier="ACTION_942_db_43"),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x80\x00\x03\x00\x01\x00\x00\x00\x03\x80')),
	Pause(1, identifier="ACTION_942_pause_45"),
	Jmp(["ACTION_942_pause_45"])
])
