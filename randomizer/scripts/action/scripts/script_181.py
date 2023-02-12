#A0181_FAST_AMANITA

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOn(),
	SetSequenceSpeed(FASTER),
	SequenceLoopingOn(),
	ShiftNortheastSteps(5),
	Pause(24),
	ShiftSouthwestSteps(5),
	Pause(72),
	ClearBit(TEMP_7044_0),
	Return()
])
