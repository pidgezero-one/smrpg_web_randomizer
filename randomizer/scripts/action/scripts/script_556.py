#A0556_BOOSTER_PASS_LAKITU_TOSSING

from randomizer.scripts.action.script_imports import *

script = ActionScript([
	SetSpriteSequence(index=3, looping=False),
	Pause(16),
	SetSpriteSequence(index=3, looping=False),
	Pause(16),
	Return()
])
