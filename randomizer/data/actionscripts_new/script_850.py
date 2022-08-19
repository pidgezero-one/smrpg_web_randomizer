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
	SetWalkingSpeed(speed=FAST),
	ShiftSouthwestPixels(4),
	ShiftSoutheastSteps(2),
	ShiftSoutheastPixels(4),
	StartLoopNTimes(17, identifier="ACTION_850_start_loop_n_times_5"),
	JumpToHeight(108),
	ShiftSoutheastSteps(2),
	EndLoop(),
	Pause(48),
	FaceSouthwest(),
	Pause(5),
	FaceNorthwest(),
	Pause(24),
	StartLoopNTimes(17),
	JumpToHeight(108),
	ShiftNorthwestSteps(2),
	EndLoop(),
	Pause(48),
	FaceNortheast(),
	Pause(5),
	FaceSoutheast(),
	Pause(24),
	Jmp(["ACTION_850_start_loop_n_times_5"])
])
