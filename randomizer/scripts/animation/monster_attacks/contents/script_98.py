# Missedme

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x3577e2"]),
	PlaySound(sound=S0116_TERRAPIN_SWING),
	SpriteSequence(sequence=4),
	PauseScriptUntilSpriteSequenceDone(),
	PlaySound(sound=S0080_WALLOP_1),
	ResetSpriteSequence(),
	RunSubroutine(["command_0x3577f2"]),
	RunSubroutine(["command_0x3523c4"]),
	ReturnSubroutine()
])
