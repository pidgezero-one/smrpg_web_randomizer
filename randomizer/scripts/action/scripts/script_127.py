#A0127_BAG_APPEARS_BRIEFLY_THEN_POOFS

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	ShadowOff(),
	FloatingOff(),
	SetVRAMPriority(PRIORITY_3),
	SetSpriteSequence(index=5, is_sequence=True, looping=True),
	VisibilityOff(),
	SequenceLoopingOn(),
	Pause(6),
	VisibilityOn(),
	Pause(26),
	SetSpriteSequence(index=6, is_sequence=True, looping=True),
	Pause(24),
	VisibilityOff(),
	Return()
])
