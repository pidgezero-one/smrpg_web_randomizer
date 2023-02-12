# ValorUp

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x3577e2"]),
	SetOMEM60To072C(),
	DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
	PlaySound(sound=S0021_SCARECROW_BIRDIES),
	SpriteSequence(sequence=4),
	PauseScriptUntilSpriteSequenceDone(),
	ResetSpriteSequence(),
	RunSubroutine(["command_0x3577f2"]),
	AttackTimerBegins(),
	ReturnSubroutine()
])
