#A0233_RIDE_YOSHI

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	FaceSoutheast(),
	SetSpriteSequence(index=5, sprite_offset=6, is_sequence=True, looping=True, mirror_sprite=True),
	Return()
])
