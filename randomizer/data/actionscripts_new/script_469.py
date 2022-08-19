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
	SetSolidityBits(cant_walk_through=True),
	SequenceLoopingOn(),
	SetSequenceSpeed(speed=NORMAL),
	StartLoopNTimes(119, identifier="ACTION_469_start_loop_n_times_3"),
	Pause(1),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=3, destinations=["ACTION_469_db_7"]),
	Jmp(["ACTION_469_end_loop_8"]),
	UnknownJmp3C(0x00, 0x20, ["ACTION_469_set_bit_11"], identifier="ACTION_469_db_7"),
	EndLoop(identifier="ACTION_469_end_loop_8"),
	TurnClockwise45DegreesNTimes(4),
	Jmp(["ACTION_469_start_loop_n_times_3"]),
	SetBit(TEMP_7044_4, identifier="ACTION_469_set_bit_11"),
	Return()
])
