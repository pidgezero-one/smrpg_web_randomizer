

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	SpriteSequence(sequence=3),
	PauseScriptUntilSpriteSequenceDone(),
	SetAMEM16BitToConst(0x60, 5),
	RunSubroutine(["command_0x3524fb"]),
	RunSubroutine(["command_0x3523c4"]),
	ResetSpriteSequence(),
	ReturnSubroutine()
])
