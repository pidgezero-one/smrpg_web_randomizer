#A0236_RIDE_YOSHI

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceWest(),
	SetSpriteSequence(index=4, sprite_offset=6, is_sequence=True, looping=True),
	Return()
])
