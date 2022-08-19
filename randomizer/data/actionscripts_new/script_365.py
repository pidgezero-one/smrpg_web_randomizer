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
	PlaySound(sound=S085_FLOWER, channel=4),
	SetVRAMPriority(PRIORITY_3),
	SetPriority(3),
	SetWalkingSpeed(speed=NORMAL),
	FloatingOff(),
	JumpToHeight(112),
	Pause(12),
	FloatingOff(),
	StartLoopNTimes(8),
	VisibilityOn(),
	Pause(4),
	VisibilityOff(),
	Pause(1),
	EndLoop(),
	Return()
])
