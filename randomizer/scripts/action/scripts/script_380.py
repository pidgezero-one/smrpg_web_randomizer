#A0380_MARRYMORE_LIBERATED_EXTERIOR_APPROACH_CHAPEL

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(SLOW, identifier="ACTION_380_set_animation_speed_0"),
	SetSequenceSpeed(NORMAL),
	ShiftNortheastSteps(3),
	SetSequenceSpeed(SLOW),
	Pause(120),
	SetSequenceSpeed(NORMAL),
	ShiftSouthwestSteps(3),
	SetSequenceSpeed(SLOW),
	FaceNortheast(),
	Pause(180),
	Jmp(["ACTION_380_set_animation_speed_0"])
])
