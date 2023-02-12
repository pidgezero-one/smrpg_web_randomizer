#A0910_FLOWER_FLASH_THEN_POOF

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FloatingOff(),
	SetSpriteSequence(index=0, is_sequence=True, looping=True),
	VisibilityOff(),
	SequenceLoopingOn(),
	Pause(9),
	VisibilityOn(),
	Pause(26),
	SetSpriteSequence(index=6, is_sequence=True, looping=True),
	Pause(24),
	VisibilityOff(),
	Return()
])
