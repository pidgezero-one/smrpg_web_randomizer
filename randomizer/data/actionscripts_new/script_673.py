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
	SetSequenceSpeed(speed=FAST),
	SetWalkingSpeed(speed=VERY_SLOW, identifier="ACTION_673_set_animation_speed_1"),
	JmpIfRandom1of2(["ACTION_673_walk_1_step_northeast_5"], identifier="ACTION_673_jmp_if_random_above_128_2"),
	Walk1StepSouthwest(),
	SetWalkingSpeed(speed=SLOW),
	Walk1StepNortheast(identifier="ACTION_673_walk_1_step_northeast_5"),
	JmpIfRandom1of2(["ACTION_673_walk_1_step_southwest_9"]),
	Walk1StepNortheast(),
	SetWalkingSpeed(speed=VERY_SLOW),
	Walk1StepSouthwest(identifier="ACTION_673_walk_1_step_southwest_9"),
	SetWalkingSpeed(speed=SLOW),
	JmpIfRandom2of3(['ACTION_673_set_animation_speed_1', 'ACTION_673_jmp_if_random_above_128_2']),
	Jmp(["ACTION_673_walk_1_step_northeast_5"])
])
