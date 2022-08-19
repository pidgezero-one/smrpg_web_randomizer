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
	FaceNortheast(),
	FixedFCoordOn(),
	SetWalkingSpeed(speed=VERY_FAST),
	StartLoopNTimes(1, identifier="ACTION_208_start_loop_n_times_3"),
	ShiftNortheastPixels(2),
	ShiftSouthwestPixels(2),
	Pause(30),
	EndLoop(),
	Pause(90),
	Jmp(["ACTION_208_start_loop_n_times_3"])
])
