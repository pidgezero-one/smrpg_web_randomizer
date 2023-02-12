#A0616_MINES_POST_LONG_TRACK_ROOM_MINECART

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSpriteSequence(index=9, is_mold=True, is_sequence=True, looping=True),
	ShiftXYPixels(x=0, y=251),
	Return()
])
