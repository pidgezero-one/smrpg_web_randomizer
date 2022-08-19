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
	SetBit(TEMP_7044_4),
	ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
	SetSolidityBits(cant_pass_walls=True),
	SetAllSpeeds(speed=NORMAL),
	SequenceLoopingOn(),
	JumpToHeight(144),
	ShiftSouthwestSteps(3),
	Pause(60),
	FixedFCoordOn(),
	SetAllSpeeds(speed=NORMAL),
	ShiftNortheastSteps(3),
	ClearBit(TEMP_7044_4),
	Return()
])
