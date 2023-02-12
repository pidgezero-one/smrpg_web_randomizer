# Defense Up!

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	InitializeBonusMessageSequence(),
	DisplayBonusMessage(message=BM_ATTACK, x=1, y=0),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=10),
	DisplayBonusMessage(message=BM_ATTACK, x=2, y=2),
	PauseScriptUntilBonusMessageComplete(),
	ReturnSubroutine()
])
