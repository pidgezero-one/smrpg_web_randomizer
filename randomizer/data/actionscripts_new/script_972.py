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
	SequenceLoopingOn(),
	ShiftNortheastSteps(2),
	Pause(24),
	FaceSoutheast(),
	Pause(24),
	FaceNorthwest(),
	Pause(24),
	FaceSouthwest(),
	Pause(24),
	FaceNortheast(),
	Pause(24),
	SetWalkingSpeed(speed=FAST),
	SetSequenceSpeed(speed=VERY_FAST),
	ShiftSouthwestSteps(2),
	Pause(8),
	SetWalkingSpeed(speed=NORMAL),
	SetSequenceSpeed(speed=FAST),
	Pause(16),
	ShiftNortheastSteps(3),
	Pause(104),
	ShiftSouthwestSteps(8),
	SetWalkingSpeed(speed=FASTER),
	ShiftNortheastSteps(7),
	FaceNorthwest(),
	SequenceLoopingOff(),
	Return()
])
