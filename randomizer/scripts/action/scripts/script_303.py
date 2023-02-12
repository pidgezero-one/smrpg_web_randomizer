#A0303_BOMB_EXPLOSION

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	TransferXYZFPixels(x=0, y=248, z=0, direction=EAST),
	SetSpriteSequence(index=1, is_sequence=True, looping=False),
	Pause(12),
	Return()
])
