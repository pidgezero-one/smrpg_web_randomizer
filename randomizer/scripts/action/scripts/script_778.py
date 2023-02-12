#A0778_PRIORITY_3_LOOPING_OFF

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetPriority(3),
	SequenceLoopingOff(),
	Return()
])
