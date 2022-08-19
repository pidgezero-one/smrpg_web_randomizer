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
	ShiftToXYCoords(x=16, y=72),
	ShadowOff(),
	FaceSouthwest(),
	SetSequenceSpeed(speed=FASTER),
	SequenceLoopingOn(),
	VisibilityOn(),
	SetPriority(3),
	ShiftSouthwestSteps(11),
	ShiftNorthwestSteps(5),
	SetPriority(2),
	Pause(8),
	ShadowOn(),
	JumpToHeight(128),
	SetWalkingSpeed(speed=FASTER),
	ShiftNorthwestSteps(5),
	Pause(64),
	SetWalkingSpeed(speed=VERY_FAST),
	SetSequenceSpeed(speed=FASTEST),
	ShiftNorthwestSteps(10),
	VisibilityOff(),
	Return()
])
