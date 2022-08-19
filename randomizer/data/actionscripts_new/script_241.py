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
	Pause(5),
	SequenceLoopingOn(),
	SetAllSpeeds(speed=FAST),
	ShiftSouthwestPixels(2),
	SetWalkingSpeed(speed=NORMAL),
	ShiftNortheastPixels(2),
	SetWalkingSpeed(speed=SLOW),
	ShiftNortheastPixels(1),
	SetSequenceSpeed(speed=SLOW),
	SetWalkingSpeed(speed=NORMAL),
	ShiftNorthPixels(2),
	SetSpriteSequence(index=4, is_mold=True, is_sequence=True),
	Pause(15),
	ShiftSouthwestPixels(1),
	SetWalkingSpeed(speed=FAST),
	ShiftSouthPixels(2),
	Pause(7),
	SetSequenceSpeed(speed=NORMAL),
	SetSpriteSequence(index=1, is_sequence=True),
	Return()
])
