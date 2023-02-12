#A0576_CURTAIN_GAME_OPEN_CURTAIN

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSpriteSequence(index=7, is_mold=True, is_sequence=True, looping=True),
	Pause(4),
	SetSpriteSequence(index=3, is_mold=True, is_sequence=True, looping=True),
	Pause(4),
	SetSpriteSequence(index=8, is_mold=True, is_sequence=True, looping=True),
	Pause(4),
	Return()
])
