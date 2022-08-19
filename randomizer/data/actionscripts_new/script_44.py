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
	Pause(55),
	FixedFCoordOn(),
	SequenceLoopingOn(),
	SetWalkingSpeed(speed=VERY_SLOW),
	SetSequenceSpeed(speed=VERY_FAST),
	ShiftNortheastPixels(8, identifier="ACTION_44_shift_northeast_pixels_5"),
	Pause(20),
	SetWalkingSpeed(speed=FAST),
	SetSequenceSpeed(speed=SLOW),
	JumpToHeight(height=40, silent=True),
	ShiftSouthwestPixels(12),
	Pause(25),
	SetWalkingSpeed(speed=VERY_SLOW),
	SetSequenceSpeed(speed=VERY_FAST),
	ShiftNortheastPixels(4),
	Jmp(["ACTION_44_shift_northeast_pixels_5"])
])
