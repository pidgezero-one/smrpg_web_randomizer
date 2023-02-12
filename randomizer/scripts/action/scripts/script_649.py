#A0649_MOLEVILLE_WOMAN_ON_MOUNTAIN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceSouthwest(),
	FixedFCoordOn(),
	SetAllSpeeds(VERY_FAST, identifier="ACTION_649_set_animation_speed_2"),
	Walk1StepSouthwest(),
	SequenceLoopingOn(),
	JmpIfObjectWithinRangeSameZ(object=MARIO, usually=0, tiles=8, destinations=["ACTION_649_start_loop_n_times_8"]),
	Pause(30),
	Jmp(["ACTION_649_set_animation_speed_14"]),
	StartLoopNTimes(4, identifier="ACTION_649_start_loop_n_times_8"),
	PlaySound(sound=SO058_INSERT, channel=4),
	Pause(2),
	PlaySound(sound=SO058_INSERT, channel=4),
	Pause(4),
	EndLoop(),
	SetAllSpeeds(SLOW, identifier="ACTION_649_set_animation_speed_14"),
	Walk1StepNortheast(),
	SequenceLoopingOff(),
	Pause(20),
	Jmp(["ACTION_649_set_animation_speed_2"])
])
