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
	SetBit(TEMP_7043_2),
	ClearSolidityBits(cant_pass_walls=True),
	VisibilityOn(),
	SequenceLoopingOn(),
	SetSequenceSpeed(speed=FAST),
	SetWalkingSpeed(speed=FASTER),
	ShiftNorthwestSteps(5),
	ShiftNorthwestPixels(5),
	Pause(24),
	FaceNortheast(),
	Pause(8),
	ShiftSoutheastSteps(5),
	ShiftSoutheastPixels(5),
	VisibilityOff(),
	Pause(48),
	ClearBit(TEMP_7043_2),
	Return()
])
