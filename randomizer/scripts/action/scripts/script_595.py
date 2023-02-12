#A0595_MIDAS_BARREL_SLOW_ANIMATION

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Db(bytearray(b'\x9a')),
	VisibilityOn(),
	SetWalkingSpeed(SLOW),
	SetSequenceSpeed(NORMAL),
	Walk1StepSouthwest(identifier="ACTION_595_walk_1_step_southwest_4"),
	Jmp(["ACTION_595_walk_1_step_southwest_4"])
])
