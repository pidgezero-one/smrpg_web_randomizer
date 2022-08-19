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
	SetBit(TEMP_7044_5),
	ClearSolidityBits(cant_pass_walls=True),
	SetWalkingSpeed(speed=FAST),
	SetSequenceSpeed(speed=VERY_FAST),
	ShiftSoutheastSteps(7),
	SetWalkingSpeed(speed=NORMAL),
	SetSequenceSpeed(speed=FAST),
	ShiftSoutheastSteps(1),
	SetWalkingSpeed(speed=SLOW),
	SetSequenceSpeed(speed=NORMAL),
	ShiftSoutheastSteps(1),
	Pause(60),
	SetWalkingSpeed(speed=NORMAL),
	SetSequenceSpeed(speed=VERY_FAST),
	ShiftNorthwestSteps(9),
	Pause(5),
	ClearBit(TEMP_7044_5),
	Return()
])
