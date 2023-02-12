#A0235_RIDE_YOSHI

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceSouth(),
	SetSpriteSequence(index=2, sprite_offset=6, is_sequence=True, looping=True),
	Return()
])
