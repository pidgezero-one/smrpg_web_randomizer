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
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_659_set_animation_speed_0"),
	SetSequenceSpeed(speed=FAST),
	StartLoopNTimes(3),
	ShiftNortheastSteps(2),
	JmpIfObjectWithinRange(object=MARIO, usually=0, tiles=4, destinations=["ACTION_659_set_animation_speed_11"]),
	EndLoop(),
	StartLoopNTimes(3),
	ShiftSouthwestSteps(2),
	JmpIfObjectWithinRange(object=MARIO, usually=0, tiles=4, destinations=["ACTION_659_set_animation_speed_11"]),
	EndLoop(),
	Jmp(["ACTION_659_set_animation_speed_0"]),
	SetSequenceSpeed(speed=VERY_FAST, identifier="ACTION_659_set_animation_speed_11"),
	SetWalkingSpeed(speed=NORMAL),
	FaceMario(),
	ShiftFDirectionSteps(2),
	Jmp(["ACTION_659_set_animation_speed_0"])
])
