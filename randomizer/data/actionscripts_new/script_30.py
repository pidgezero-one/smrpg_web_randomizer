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
	SetSequenceSpeed(speed=SLOW, identifier="ACTION_30_set_animation_speed_0"),
	SequenceLoopingOn(),
	SetWalkingSpeed(speed=VERY_SLOW),
	Walk1StepSoutheast(),
	JmpIfRandom1of2(["ACTION_30_pause_8"]),
	Walk1StepNorthwest(identifier="ACTION_30_walk_1_step_northwest_5"),
	JmpIfRandom1of2(["ACTION_30_pause_14"]),
	Jmp(["ACTION_30_set_animation_speed_0"]),
	Pause(30, identifier="ACTION_30_pause_8"),
	FaceNortheast(),
	Pause(30),
	FaceSouthwest(),
	Pause(30),
	Jmp(["ACTION_30_walk_1_step_northwest_5"]),
	Pause(30, identifier="ACTION_30_pause_14"),
	FaceSouthwest(),
	Pause(30),
	FaceNortheast(),
	Pause(30),
	Jmp(["ACTION_30_set_animation_speed_0"])
])
