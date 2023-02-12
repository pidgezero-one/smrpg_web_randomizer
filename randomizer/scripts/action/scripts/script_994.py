#A0994_KEEP_BRIDGE_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(VERY_FAST, identifier="ACTION_994_set_animation_speed_0"),
	SetWalkingSpeed(NORMAL),
	ShiftNortheastSteps(3),
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(SLOW),
	ShiftNortheastSteps(2),
	ShiftSoutheastSteps(1),
	ShiftSouthwestSteps(3),
	FaceSoutheast(),
	FixedFCoordOn(),
	SetSequenceSpeed(NORMAL),
	SetWalkingSpeed(VERY_SLOW),
	ShiftSouthwestSteps(2),
	FixedFCoordOff(),
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(SLOW),
	ShiftSouthwestSteps(6),
	ShiftNorthwestSteps(1),
	ShiftNortheastSteps(6),
	Jmp(["ACTION_994_set_animation_speed_0"])
])
