#A0431_YOSHI_RACE_ANIMATION

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(NORMAL, identifier="ACTION_431_set_animation_speed_0"),
	SequenceLoopingOn(),
	ResetProperties(),
	SetObjectMemoryBits(arg_1=0x0E, bits=[2, 3]),
	Pause(1, identifier="ACTION_431_pause_4"),
	Jmp(["ACTION_431_pause_4"])
])
