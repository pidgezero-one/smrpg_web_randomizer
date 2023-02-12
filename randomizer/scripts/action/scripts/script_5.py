#A0005_SHIP_SHOP_SHAMAN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	TurnRandomDirection(identifier="ACTION_5_turn_random_direction_0"),
	Walk1StepFDirection(identifier="ACTION_5_walk_1_step_f_direction_1"),
	Pause(30, identifier="ACTION_5_pause_2"),
	JmpIfRandom1of2(["ACTION_5_pause_2"]),
	JmpIfRandom1of2(["ACTION_5_walk_1_step_f_direction_1"]),
	JmpIfRandom2of3(['ACTION_5_set_animation_speed_8', 'ACTION_5_set_animation_speed_10']),
	SetWalkingSpeed(SLOW),
	Jmp(["ACTION_5_turn_random_direction_0"]),
	SetWalkingSpeed(VERY_SLOW, identifier="ACTION_5_set_animation_speed_8"),
	Jmp(["ACTION_5_turn_random_direction_0"]),
	SetWalkingSpeed(NORMAL, identifier="ACTION_5_set_animation_speed_10"),
	Jmp(["ACTION_5_turn_random_direction_0"])
])
