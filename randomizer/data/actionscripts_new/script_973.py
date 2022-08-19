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
	SequenceLoopingOn(),
	Walk1StepNortheast(),
	ShiftNorthwestSteps(2),
	ShiftSouthwestSteps(2),
	ShiftSoutheastSteps(3),
	ShiftSoutheastPixels(8),
	ShiftNortheastSteps(5),
	Walk1StepNorthwest(),
	SetWalkingSpeed(speed=VERY_FAST),
	ShiftSouthwestSteps(3),
	FaceNorthwest(),
	JumpToHeight(64),
	Pause(32),
	SequenceLoopingOff(),
	Return()
])
