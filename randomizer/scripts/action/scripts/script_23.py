#A0023_FAST_REPEATED_JUMPING

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(VERY_FAST, identifier="ACTION_23_set_animation_speed_0"),
	AddZCoord1Step(),
	DecZCoord1Step(),
	Jmp(["ACTION_23_set_animation_speed_0"])
])
