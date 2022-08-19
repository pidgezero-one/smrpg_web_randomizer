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
	ShiftToXYCoords(x=25, y=7),
	ShadowOff(),
	FaceSouthwest(),
	SetSequenceSpeed(speed=VERY_FAST),
	SequenceLoopingOn(),
	VisibilityOn(),
	ShiftSouthwestSteps(4),
	SetPriority(3),
	StartLoopNTimes(2),
	ShiftSoutheastSteps(4),
	ShiftSouthwestSteps(8),
	EndLoop(),
	Pause(8),
	ShadowOn(),
	JumpToHeight(128),
	SetWalkingSpeed(speed=FASTER),
	ShiftSouthwestSteps(5),
	Pause(56),
	SetWalkingSpeed(speed=VERY_FAST),
	SetSequenceSpeed(speed=FASTEST),
	ShiftSouthwestSteps(32),
	VisibilityOff(),
	Return()
])
