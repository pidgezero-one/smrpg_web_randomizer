#A0539_MUSHROOM_WAY_2_TROOPA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FloatingOff(identifier="ACTION_539_floating_off_0"),
	SequenceLoopingOn(),
	SetSequenceSpeed(FAST),
	SetWalkingSpeed(SLOW),
	FaceMario(),
	Pause(10),
	ShiftFDirectionSteps(2),
	Pause(10),
	Jmp(["ACTION_539_floating_off_0"])
])
