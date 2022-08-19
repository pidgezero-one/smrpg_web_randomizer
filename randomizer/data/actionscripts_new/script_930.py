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
	FixedFCoordOn(),
	Set700CToObjectCoord(object=DUMMY_0X07, coord=F, pixel=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_930_set_sprite_sequence_5"]),
	SetSpriteSequence(index=0, is_sequence=True),
	Jmp(["ACTION_930_start_loop_n_times_6"]),
	SetSpriteSequence(index=0, is_sequence=True, mirror_sprite=True, identifier="ACTION_930_set_sprite_sequence_5"),
	StartLoopNTimes(47, identifier="ACTION_930_start_loop_n_times_6"),
	Pause(1),
	JmpIfMarioInAir(["ACTION_930_ret_23"]),
	EndLoop(),
	StartLoopNTimes(11),
	SetWalkingSpeed(speed=FAST),
	ShiftZDownPixels(2),
	ShiftZUpPixels(2),
	JmpIfMarioInAir(["ACTION_930_ret_23"]),
	EndLoop(),
	JumpToHeight(height=0, silent=True),
	FloatingOn(),
	Pause(1, identifier="ACTION_930_pause_18"),
	JmpIfObjectInAir(DUMMY_0X07, ["ACTION_930_pause_18"]),
	ClearSolidityBits(cant_pass_walls=True, bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	VisibilityOff(),
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	Return(identifier="ACTION_930_ret_23")
])
