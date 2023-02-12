#A0521_TOWER_BEETLE

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(VERY_SLOW, identifier="ACTION_521_set_animation_speed_0"),
	ShiftNorthwestPixels(6),
	Pause(30),
	ShiftSouthwestPixels(6),
	Pause(20),
	ShiftSoutheastPixels(6),
	Pause(40),
	ShiftNortheastPixels(6),
	Pause(15),
	Jmp(["ACTION_521_set_animation_speed_0"])
])
