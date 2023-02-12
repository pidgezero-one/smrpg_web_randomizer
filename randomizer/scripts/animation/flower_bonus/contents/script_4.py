# Once Again!

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	InitializeBonusMessageSequence(),
	DisplayBonusMessage(message=BM_ATTACK, x=4, y=0),
	DisplayBonusMessage(message=BM_ATTACK, x=5, y=4),
	PauseScriptUntilBonusMessageComplete(),
	ReturnSubroutine()
])
