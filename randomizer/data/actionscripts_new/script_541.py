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
	SetBit(TEMP_7044_3),
	ClearSolidityBits(cant_pass_walls=True),
	SetAllSpeeds(speed=VERY_FAST),
	ShiftSouthwestSteps(2),
	SetWalkingSpeed(speed=FAST),
	SetSequenceSpeed(speed=VERY_FAST),
	ShiftSouthwestSteps(6),
	SetWalkingSpeed(speed=NORMAL),
	SetSequenceSpeed(speed=FAST),
	ShiftSouthwestSteps(1),
	SetWalkingSpeed(speed=SLOW),
	SetSequenceSpeed(speed=NORMAL),
	ShiftSouthwestSteps(1),
	Pause(60),
	SetWalkingSpeed(speed=NORMAL),
	SetSequenceSpeed(speed=VERY_FAST),
	ShiftNortheastSteps(10),
	ClearBit(TEMP_7044_3),
	Return()
])
