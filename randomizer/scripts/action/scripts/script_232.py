#A0232_RIDE_YOSHI

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceSouthwest(),
	SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=True),
	Return()
])
