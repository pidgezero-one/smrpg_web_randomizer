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
	ShiftToXYCoords(x=3, y=51),
	ShadowOff(),
	FaceNortheast(),
	SetSequenceSpeed(speed=VERY_FAST),
	SequenceLoopingOn(),
	VisibilityOn(),
	ShiftNortheastSteps(8),
	ShiftSoutheastSteps(4),
	ShiftNortheastSteps(12),
	ShiftNorthwestSteps(12),
	ShiftNortheastSteps(4),
	FaceNorthwest(),
	Pause(8),
	ShadowOn(),
	JumpToHeight(128),
	SetWalkingSpeed(speed=FASTER),
	ShiftNorthwestSteps(5),
	Pause(56),
	SetWalkingSpeed(speed=VERY_FAST),
	SetSequenceSpeed(speed=FASTEST),
	ShiftNorthwestSteps(8),
	VisibilityOff(),
	Return()
])
