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
	FixedFCoordOn(),
	SetWalkingSpeed(speed=VERY_FAST),
	Pause(90, identifier="ACTION_209_pause_2"),
	StartLoopNTimes(1),
	ShiftSouthwestPixels(2),
	ShiftNortheastPixels(2),
	Pause(30),
	EndLoop(),
	Jmp(["ACTION_209_pause_2"])
])
