#A0793_DEFAULT_SEQUENCE_STATIC

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOff(),
	SequenceLoopingOn(),
	SetPriority(3),
	VisibilityOn(),
	SetSolidityBits(cant_jump_through=True),
	Pause(1, identifier="ACTION_793_pause_8"),
	Jmp(["ACTION_793_pause_8"])
])
