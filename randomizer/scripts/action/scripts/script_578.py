#A0578_CURTAIN_GAME_HENCHMAN_SPIN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(FAST, identifier="ACTION_578_set_animation_speed_0"),
	SequenceLoopingOn(),
	FaceNorthwest(),
	Pause(46),
	FaceNortheast(),
	Pause(32),
	FaceNorthwest(),
	Pause(31),
	FaceNortheast(),
	Pause(50),
	FaceNorthwest(),
	Pause(24),
	FaceNortheast(),
	Pause(22),
	Jmp(["ACTION_578_set_animation_speed_0"])
])
