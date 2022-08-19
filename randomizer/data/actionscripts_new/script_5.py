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
	TurnRandomDirection(identifier="ACTION_5_turn_random_direction_0"),
	Walk1StepFDirection(identifier="ACTION_5_walk_1_step_f_direction_1"),
	Pause(30, identifier="ACTION_5_pause_2"),
	JmpIfRandom1of2(["ACTION_5_pause_2"]),
	JmpIfRandom1of2(["ACTION_5_walk_1_step_f_direction_1"]),
	JmpIfRandom2of3(['ACTION_5_set_animation_speed_8', 'ACTION_5_set_animation_speed_10']),
	SetWalkingSpeed(speed=SLOW),
	Jmp(["ACTION_5_turn_random_direction_0"]),
	SetWalkingSpeed(speed=VERY_SLOW, identifier="ACTION_5_set_animation_speed_8"),
	Jmp(["ACTION_5_turn_random_direction_0"]),
	SetWalkingSpeed(speed=NORMAL, identifier="ACTION_5_set_animation_speed_10"),
	Jmp(["ACTION_5_turn_random_direction_0"])
])
