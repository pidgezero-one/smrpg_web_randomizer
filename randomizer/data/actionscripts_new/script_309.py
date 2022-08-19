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
	VisibilityOff(identifier="ACTION_309_visibility_off_0"),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	Set700CToPressedButton(),
	Mem700CAndConst(0x0003),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["ACTION_309_jmp_if_random_above_128_11"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_309_pause_10"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_309_pause_9"]),
	Pause(3),
	Pause(3, identifier="ACTION_309_pause_9"),
	Pause(3, identifier="ACTION_309_pause_10"),
	JmpIfRandom1of2(["ACTION_309_add_z_coord_1_step_15"], identifier="ACTION_309_jmp_if_random_above_128_11"),
	DecZCoord1Step(identifier="ACTION_309_dec_z_coord_1_step_12"),
	JmpIfRandom1of2(["ACTION_309_dec_z_coord_1_step_12"]),
	Jmp(["ACTION_309_set_700C_to_object_coord_17"]),
	AddZCoord1Step(identifier="ACTION_309_add_z_coord_1_step_15"),
	JmpIfRandom1of2(["ACTION_309_add_z_coord_1_step_15"]),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=Z, pixel=True, bit_7=True, identifier="ACTION_309_set_700C_to_object_coord_17"),
	CompareVarToConst(PRIMARY_TEMP_700C, 8),
	JmpIfComparisonResultIsGreaterOrEqual(["ACTION_309_visibility_off_0"]),
	FaceMario(),
	PlaySound(sound=S044_GHOST_FLOAT, channel=4),
	StartLoopNTimes(3),
	VisibilityOn(),
	Pause(2),
	VisibilityOff(),
	Pause(2),
	EndLoop(),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	VisibilityOn(),
	SequenceLoopingOn(identifier="ACTION_309_sequence_looping_on_31"),
	ShiftFDirectionSteps(2),
	JmpIfRandom1of2(["ACTION_309_sequence_looping_on_31"]),
	StartLoopNTimes(3),
	TurnRandomDirection(),
	Pause(16),
	EndLoop(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	StartLoopNTimes(3),
	VisibilityOff(),
	Pause(2),
	VisibilityOn(),
	Pause(2),
	EndLoop(),
	Jmp(["ACTION_309_visibility_off_0"])
])
