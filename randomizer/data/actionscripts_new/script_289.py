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
	SetSequenceSpeed(speed=SLOW),
	SetObjectMemoryBits(arg_1=0x0E),
	SetSolidityBits(cant_pass_walls=True),
	ClearBit(TEMP_7044_0),
	ClearBit(TEMP_7044_1),
	ClearBit(TEMP_7044_2),
	ClearBit(TEMP_7044_3),
	ClearBit(TEMP_7044_5),
	Pause(12),
	SetSequenceSpeed(speed=SLOW),
	SetWalkingSpeed(speed=NORMAL),
	SequenceLoopingOn(),
	SetSolidityBits(cant_walk_through=True),
	ClearSolidityBits(cant_pass_npcs=True),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_700C),
	FaceEast7C(),
	Return()
])
