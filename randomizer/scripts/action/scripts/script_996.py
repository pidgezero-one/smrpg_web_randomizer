#A0996_KEEP_BRIDGE_GOOMBA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSequenceSpeed(FAST, identifier="ACTION_996_set_animation_speed_0"),
	SetWalkingSpeed(SLOW),
	ShiftSouthwestSteps(5),
	ShiftNorthwestSteps(1),
	ShiftNortheastSteps(11),
	ShiftSoutheastSteps(1),
	ShiftSouthwestSteps(1),
	FaceNortheast(),
	FixedFCoordOn(),
	SetSequenceSpeed(NORMAL),
	SetWalkingSpeed(VERY_SLOW),
	ShiftSouthwestSteps(2),
	FixedFCoordOff(),
	SetSequenceSpeed(VERY_FAST),
	SetWalkingSpeed(NORMAL),
	ShiftSouthwestSteps(3),
	Jmp(["ACTION_996_set_animation_speed_0"])
])
