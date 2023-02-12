#A0673_PIPE_VAULT_FINAL_ROOM_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(VERY_SLOW, identifier="ACTION_673_set_animation_speed_1"),
	JmpIfRandom1of2(["ACTION_673_walk_1_step_northeast_5"], identifier="ACTION_673_jmp_if_random_above_128_2"),
	Walk1StepSouthwest(),
	SetWalkingSpeed(SLOW),
	Walk1StepNortheast(identifier="ACTION_673_walk_1_step_northeast_5"),
	JmpIfRandom1of2(["ACTION_673_walk_1_step_southwest_9"]),
	Walk1StepNortheast(),
	SetWalkingSpeed(VERY_SLOW),
	Walk1StepSouthwest(identifier="ACTION_673_walk_1_step_southwest_9"),
	SetWalkingSpeed(SLOW),
	JmpIfRandom2of3(['ACTION_673_set_animation_speed_1', 'ACTION_673_jmp_if_random_above_128_2']),
	Jmp(["ACTION_673_walk_1_step_northeast_5"])
])
