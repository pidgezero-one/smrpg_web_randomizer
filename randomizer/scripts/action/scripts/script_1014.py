#A1014_KEEP_DARK_ROOM_TROOPA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(VERY_FAST, identifier="ACTION_1014_set_animation_speed_0"),
	SetWalkingSpeed(FAST),
	ShiftSoutheastSteps(5),
	ShiftNortheastSteps(6),
	ShiftSoutheastSteps(4),
	ShiftSouthwestSteps(3),
	ShiftNorthwestSteps(9),
	ShiftNortheastSteps(3),
	ShiftSoutheastSteps(10),
	ShiftSouthwestSteps(6),
	ShiftNorthwestSteps(10),
	BounceToXYWithHeight(x=17, y=27, height=2),
	Jmp(["ACTION_1014_set_animation_speed_0"])
])
