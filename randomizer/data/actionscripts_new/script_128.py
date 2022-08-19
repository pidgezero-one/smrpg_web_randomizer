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
	SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1], identifier="ACTION_128_set_object_memory_bits_0"),
	SetSolidityBits(cant_pass_walls=True),
	JmpIfRandom2of3(['ACTION_128_set_animation_speed_5', 'ACTION_128_pause_13']),
	SetWalkingSpeed(speed=SLOW),
	Walk1StepSoutheast(),
	SetWalkingSpeed(speed=VERY_SLOW, identifier="ACTION_128_set_animation_speed_5"),
	TurnRandomDirection(),
	Walk1StepFDirection(),
	JmpIfRandom1of2(["ACTION_128_set_animation_speed_14"]),
	Walk1StepSoutheast(identifier="ACTION_128_walk_1_step_southeast_9"),
	Pause(30),
	JmpIfRandom1of2(["ACTION_128_set_animation_speed_14"]),
	Walk1StepNortheast(identifier="ACTION_128_walk_1_step_northeast_12"),
	Pause(60, identifier="ACTION_128_pause_13"),
	SetWalkingSpeed(speed=VERY_SLOW, identifier="ACTION_128_set_animation_speed_14"),
	JmpIfRandom2of3(['ACTION_128_walk_1_step_northwest_23', 'ACTION_128_walk_1_step_northeast_12']),
	Walk1StepSouthwest(),
	Pause(20),
	JmpIfRandom1of2(["ACTION_128_set_object_memory_bits_0"]),
	Pause(30),
	JmpIfRandom2of3(['ACTION_128_walk_1_step_southeast_9', 'ACTION_128_pause_25']),
	SetWalkingSpeed(speed=SLOW),
	Walk1StepNortheast(),
	Walk1StepNorthwest(identifier="ACTION_128_walk_1_step_northwest_23"),
	Jmp(["ACTION_128_set_animation_speed_14"]),
	Pause(60, identifier="ACTION_128_pause_25"),
	SetWalkingSpeed(speed=VERY_SLOW),
	ShiftNortheastSteps(2),
	Jmp(["ACTION_128_set_animation_speed_14"])
])
