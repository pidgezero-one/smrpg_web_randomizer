#A0349_STATIC_RAT

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SequenceLoopingOn(identifier="ACTION_349_sequence_looping_on_0"),
	FaceMario(),
	Pause(2),
	Jmp(["ACTION_349_sequence_looping_on_0"])
])
