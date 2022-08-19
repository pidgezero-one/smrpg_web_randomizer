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
	SetWalkingSpeed(speed=FAST),
	ShiftNortheastPixels(2),
	ShiftSouthwestPixels(2),
	SetWalkingSpeed(speed=SLOW),
	ShiftZDownPixels(2),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftZDownPixels(2),
	Pause(17),
	SetWalkingSpeed(speed=FAST),
	ShiftZUpPixels(4),
	ShiftNortheastPixels(2),
	SetWalkingSpeed(speed=NORMAL),
	ShiftSouthwestPixels(4),
	SetWalkingSpeed(speed=SLOW),
	ShiftNortheastPixels(2),
	Return()
])
