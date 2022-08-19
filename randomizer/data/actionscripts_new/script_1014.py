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
	SetSequenceSpeed(speed=VERY_FAST, identifier="ACTION_1014_set_animation_speed_0"),
	SetWalkingSpeed(speed=FAST),
	ShiftSoutheastSteps(5),
	ShiftNortheastSteps(6),
	ShiftSoutheastSteps(4),
	ShiftSouthwestSteps(3),
	ShiftNorthwestSteps(9),
	ShiftNortheastSteps(3),
	ShiftSoutheastSteps(10),
	ShiftSouthwestSteps(6),
	ShiftNorthwestSteps(10),
	BounceToXYWithHeight(x=17, y=27, height=2),
	Jmp(["ACTION_1014_set_animation_speed_0"])
])
