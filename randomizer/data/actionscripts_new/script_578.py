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
	SetSequenceSpeed(speed=FAST, identifier="ACTION_578_set_animation_speed_0"),
	SequenceLoopingOn(),
	FaceNorthwest(),
	Pause(46),
	FaceNortheast(),
	Pause(32),
	FaceNorthwest(),
	Pause(31),
	FaceNortheast(),
	Pause(50),
	FaceNorthwest(),
	Pause(24),
	FaceNortheast(),
	Pause(22),
	Jmp(["ACTION_578_set_animation_speed_0"])
])
