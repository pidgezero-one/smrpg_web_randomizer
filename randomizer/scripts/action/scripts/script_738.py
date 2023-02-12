#A0738_TOWER_CHEST_SEESAW_WHEN_ACTIVATED

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	Pause(1),
	SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True),
	Return()
])
