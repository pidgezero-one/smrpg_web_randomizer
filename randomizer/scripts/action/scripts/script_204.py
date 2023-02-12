#A0204_SEQUENCE_2_FALL

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	VisibilityOff(),
	SetSpriteSequence(index=2, is_sequence=True, looping=True),
	Jmp(["ACTION_917_pause_2"])
])
