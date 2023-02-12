#A0209_RAINI_ENDING

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FixedFCoordOn(),
	SetWalkingSpeed(VERY_FAST),
	Pause(90, identifier="ACTION_209_pause_2"),
	StartLoopNTimes(1),
	ShiftSouthwestPixels(2),
	ShiftNortheastPixels(2),
	Pause(30),
	EndLoop(),
	Jmp(["ACTION_209_pause_2"])
])
