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
	ClearBit(TEMP_7042_0),
	ClearBit(TEMP_7042_1),
	ClearBit(TEMP_7042_2),
	ClearBit(TEMP_7042_3),
	ClearBit(TEMP_7042_4),
	ClearBit(TEMP_7042_5),
	ClearBit(TEMP_7042_7),
	SetSequenceSpeed(speed=FAST),
	SetWalkingSpeed(speed=NORMAL),
	ShiftNorthwestSteps(2),
	ShiftNortheastSteps(3),
	ShiftNorthwestSteps(4),
	ShiftSouthwestSteps(2),
	FaceSoutheast(),
	SetSequenceSpeed(speed=SLOW),
	ClearBit(TEMP_7043_1),
	Return()
])
