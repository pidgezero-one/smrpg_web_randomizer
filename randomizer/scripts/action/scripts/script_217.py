#A0217_GREEN_YOSHI

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceSoutheast(),
	SetSequenceSpeed(FAST),
	SequenceLoopingOn(),
	SetVarToConst(ROSE_WAY_703E, 1),
	Return()
])
