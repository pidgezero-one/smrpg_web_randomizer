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
	SetWalkingSpeed(speed=VERY_SLOW, identifier="ACTION_98_set_animation_speed_0"),
	Walk1StepSouthwest(),
	JmpIfRandom1of2(["ACTION_98_pause_6"]),
	Walk1StepNortheast(identifier="ACTION_98_walk_1_step_northeast_3"),
	JmpIfRandom1of2(["ACTION_98_pause_12"]),
	Jmp(["ACTION_98_set_animation_speed_0"]),
	Pause(30, identifier="ACTION_98_pause_6"),
	FaceNorthwest(),
	Pause(30),
	FaceSoutheast(),
	Pause(30),
	Jmp(["ACTION_98_walk_1_step_northeast_3"]),
	Pause(30, identifier="ACTION_98_pause_12"),
	FaceSoutheast(),
	Pause(30),
	FaceNorthwest(),
	Pause(30),
	Jmp(["ACTION_98_set_animation_speed_0"])
])
