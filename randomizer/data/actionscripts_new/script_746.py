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
	ShiftToXYCoords(x=12, y=120),
	ShadowOff(),
	FaceNorthwest(),
	SetSequenceSpeed(speed=VERY_FAST),
	SequenceLoopingOn(),
	VisibilityOn(),
	ShiftNorthwestSteps(12),
	ShiftNortheastSteps(3),
	WalkToXYCoords(x=8, y=95),
	ShiftNorthPixels(4),
	ShiftNortheastSteps(12),
	Pause(8),
	ShadowOn(),
	JumpToHeight(128),
	SetWalkingSpeed(speed=FASTER),
	ShiftNortheastSteps(5),
	Pause(56),
	SetWalkingSpeed(speed=VERY_FAST),
	SetSequenceSpeed(speed=FASTEST),
	ShiftNortheastSteps(8),
	VisibilityOff(),
	Return()
])
