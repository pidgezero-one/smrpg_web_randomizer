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
	Pause(1, identifier="ACTION_519_placeholder"),
	FaceSouthwest(),
	FixedFCoordOn(),
	Pause(120),
	SetWalkingSpeed(speed=NORMAL),
	ShiftSouthPixels(15),
	Pause(120),
	Pause(120),
	Pause(120),
	Pause(120),
	ShiftNorthPixels(15),
	Pause(60),
	Jmp(["ACTION_519_placeholder"]),
	VisibilityOff(),
	Return()
])
