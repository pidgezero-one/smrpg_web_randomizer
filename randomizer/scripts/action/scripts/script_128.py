#A0128_WALK_RANDOM_DIRECTIONS

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1], identifier="ACTION_128_set_object_memory_bits_0"),
	SetSolidityBits(cant_pass_walls=True),
	JmpIfRandom2of3(['ACTION_128_set_animation_speed_5', 'ACTION_128_pause_13']),
	SetWalkingSpeed(SLOW),
	Walk1StepSoutheast(),
	SetWalkingSpeed(VERY_SLOW, identifier="ACTION_128_set_animation_speed_5"),
	TurnRandomDirection(),
	Walk1StepFDirection(),
	JmpIfRandom1of2(["ACTION_128_set_animation_speed_14"]),
	Walk1StepSoutheast(identifier="ACTION_128_walk_1_step_southeast_9"),
	Pause(30),
	JmpIfRandom1of2(["ACTION_128_set_animation_speed_14"]),
	Walk1StepNortheast(identifier="ACTION_128_walk_1_step_northeast_12"),
	Pause(60, identifier="ACTION_128_pause_13"),
	SetWalkingSpeed(VERY_SLOW, identifier="ACTION_128_set_animation_speed_14"),
	JmpIfRandom2of3(['ACTION_128_walk_1_step_northwest_23', 'ACTION_128_walk_1_step_northeast_12']),
	Walk1StepSouthwest(),
	Pause(20),
	JmpIfRandom1of2(["ACTION_128_set_object_memory_bits_0"]),
	Pause(30),
	JmpIfRandom2of3(['ACTION_128_walk_1_step_southeast_9', 'ACTION_128_pause_25']),
	SetWalkingSpeed(SLOW),
	Walk1StepNortheast(),
	Walk1StepNorthwest(identifier="ACTION_128_walk_1_step_northwest_23"),
	Jmp(["ACTION_128_set_animation_speed_14"]),
	Pause(60, identifier="ACTION_128_pause_25"),
	SetWalkingSpeed(VERY_SLOW),
	ShiftNortheastSteps(2),
	Jmp(["ACTION_128_set_animation_speed_14"])
])
