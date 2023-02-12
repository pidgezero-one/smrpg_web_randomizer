# HP Max!

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	InitializeBonusMessageSequence(),
	DisplayBonusMessage(message=BM_ATTACK, x=3, y=4),
	PauseScriptUntilBonusMessageComplete(),
	ReturnSubroutine()
])
