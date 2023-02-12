#A0779_LANDS_END_MOVING_CHEST

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(3),
	FixedFCoordOn(),
	Db(bytearray(b' \x04')),
	EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x08\x80')),
	SetWalkingSpeed(VERY_SLOW),
	Walk1StepNortheast(identifier="ACTION_779_walk_1_step_northeast_5"),
	Walk1StepSouthwest(),
	Jmp(["ACTION_779_walk_1_step_northeast_5"])
])
