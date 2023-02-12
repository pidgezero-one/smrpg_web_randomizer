#A0030_POST_THRONE_BIRDS_3_TO_7

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(SLOW, identifier="ACTION_30_set_animation_speed_0"),
	SequenceLoopingOn(),
	SetWalkingSpeed(VERY_SLOW),
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
