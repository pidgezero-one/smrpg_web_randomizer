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
	SetSequenceSpeed(speed=NORMAL, identifier="ACTION_1002_set_animation_speed_0"),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftNorthwestPixels(8),
	ShiftNorthwestSteps(2),
	SetSequenceSpeed(speed=SLOW),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftNorthwestSteps(1),
	FaceSoutheast(),
	Pause(10),
	SetSequenceSpeed(speed=NORMAL),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftSoutheastSteps(2),
	ShiftSoutheastPixels(8),
	SetSequenceSpeed(speed=SLOW),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftSoutheastSteps(1),
	FaceNorthwest(),
	Pause(10),
	Jmp(["ACTION_1002_set_animation_speed_0"])
])
