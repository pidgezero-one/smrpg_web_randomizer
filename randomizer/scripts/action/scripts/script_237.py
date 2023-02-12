#A0237_RIDE_YOSHI

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceEast(),
	SetSpriteSequence(index=4, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True),
	Return()
])
