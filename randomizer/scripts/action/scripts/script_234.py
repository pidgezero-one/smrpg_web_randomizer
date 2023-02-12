#A0234_RIDE_YOSHI

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceNorth(),
	SetSpriteSequence(index=3, sprite_offset=6, is_sequence=True, looping=True),
	Return()
])
