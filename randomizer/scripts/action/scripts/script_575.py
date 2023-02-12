#A0575_MONSTRO_LAIR_TRANSPARENCY_LAYER

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetWalkingSpeed(VERY_FAST),
	ShiftEastSteps(10, identifier="ACTION_575_shift_east_steps_1"),
	Jmp(["ACTION_575_shift_east_steps_1"])
])
