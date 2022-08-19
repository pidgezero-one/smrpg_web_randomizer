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
	SetWalkingSpeed(speed=SLOW, identifier="ACTION_887_set_animation_speed_0"),
	SetSequenceSpeed(speed=NORMAL),
	ShiftSoutheastSteps(3),
	JmpIfRandom1of2(["ACTION_887_walk_1_step_southwest_5"]),
	Pause(60),
	Walk1StepSouthwest(identifier="ACTION_887_walk_1_step_southwest_5"),
	JmpIfRandom1of2(["ACTION_887_shift_northwest_steps_8"]),
	Pause(30),
	ShiftNorthwestSteps(3, identifier="ACTION_887_shift_northwest_steps_8"),
	JmpIfRandom1of2(["ACTION_887_walk_1_step_northeast_11"]),
	Pause(30),
	Walk1StepNortheast(identifier="ACTION_887_walk_1_step_northeast_11"),
	Jmp(["ACTION_887_set_animation_speed_0"])
])
