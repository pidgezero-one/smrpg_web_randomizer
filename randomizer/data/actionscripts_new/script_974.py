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
	SetSequenceSpeed(speed=FAST),
	SetWalkingSpeed(speed=SLOW),
	ShiftSoutheastSteps(2),
	ShiftNortheastSteps(2),
	Walk1StepSoutheast(),
	SetWalkingSpeed(speed=FAST),
	ShiftSoutheastSteps(2),
	ShiftSouthwestSteps(3),
	SetWalkingSpeed(speed=SLOW),
	ShiftNorthwestSteps(5),
	ShiftNorthwestPixels(8),
	Walk1StepSouthwest(),
	ShiftSoutheastPixels(8),
	Pause(24),
	SequenceLoopingOn(),
	JumpToHeight(64),
	Pause(32),
	FaceNorthwest(),
	Pause(32),
	SequenceLoopingOff(),
	Return()
])
