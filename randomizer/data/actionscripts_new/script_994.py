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
	SetSequenceSpeed(speed=VERY_FAST, identifier="ACTION_994_set_animation_speed_0"),
	SetWalkingSpeed(speed=NORMAL),
	ShiftNortheastSteps(3),
	SetSequenceSpeed(speed=FAST),
	SetWalkingSpeed(speed=SLOW),
	ShiftNortheastSteps(2),
	ShiftSoutheastSteps(1),
	ShiftSouthwestSteps(3),
	FaceSoutheast(),
	FixedFCoordOn(),
	SetSequenceSpeed(speed=NORMAL),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftSouthwestSteps(2),
	FixedFCoordOff(),
	SetSequenceSpeed(speed=FAST),
	SetWalkingSpeed(speed=SLOW),
	ShiftSouthwestSteps(6),
	ShiftNorthwestSteps(1),
	ShiftNortheastSteps(6),
	Jmp(["ACTION_994_set_animation_speed_0"])
])
