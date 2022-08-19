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
	SetWalkingSpeed(speed=FASTEST),
	ShiftSouthPixels(8),
	SetBit(TEMP_7043_2),
	ShiftNorthPixels(16),
	ShiftSouthPixels(16),
	ShiftNorthPixels(12),
	ShiftSouthPixels(8),
	ClearBit(TEMP_7043_2),
	ShiftNorthPixels(8),
	ShiftSouthPixels(6),
	ShiftNorthPixels(4),
	ShiftSouthPixels(4),
	ShiftNorthPixels(2),
	Return()
])
