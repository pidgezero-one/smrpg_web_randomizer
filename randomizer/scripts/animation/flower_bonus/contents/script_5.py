# Lucky!

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	InitializeBonusMessageSequence(),
	DisplayBonusMessage(message=BM_ATTACK, x=6, y=2),
	PauseScriptUntilBonusMessageComplete(),
	ReturnSubroutine()
])
