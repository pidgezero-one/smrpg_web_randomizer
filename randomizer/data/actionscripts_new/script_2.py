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
	ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	JmpIfBitClear(TEMP_707C_1, ["ACTION_2_start_loop_n_times_3"]),
	ClearSolidityBits(bit_4=True, cant_walk_through=True),
	StartLoopNTimes(15, identifier="ACTION_2_start_loop_n_times_3"),
	Pause(2),
	VisibilityOff(),
	Pause(2),
	VisibilityOn(),
	EndLoop(),
	SetSolidityBits(bit_4=True, cant_walk_through=True),
	ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	Return()
])
