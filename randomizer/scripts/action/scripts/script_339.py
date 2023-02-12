#A0339_SHIP_TRAMPOLINE_PUZZLE_CANNONBALL

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSpriteSequence(index=2, is_sequence=True, looping=False),
	IncPaletteRowBy(3),
	Return()
])
