#A0580_CURTAIN_GAME_HENCHMAN_SPIN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(FAST, identifier="ACTION_580_set_animation_speed_0"),
	SequenceLoopingOn(),
	FaceSouthwest(),
	Pause(15),
	FaceNorthwest(),
	Pause(50),
	FaceSouthwest(),
	Pause(31),
	FaceNorthwest(),
	Pause(45),
	FaceSouthwest(),
	Pause(37),
	FaceNorthwest(),
	Pause(22),
	Jmp(["ACTION_580_set_animation_speed_0"])
])
