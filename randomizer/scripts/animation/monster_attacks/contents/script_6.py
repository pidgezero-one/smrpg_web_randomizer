# PhysicalAttack8

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	PlaySound(sound=S0097_PLASMA_TOSS),
	RunSubroutine(["command_0x35791e"]),
	SetAMEM8BitTo7E1x(0x6F, 0x7EE00F),
	JmpIfAMEM8BitEqualsConst(0x6F, 1, ["command_0x351625"]),
	RunSubroutine(["command_0x353140"]),
	Jmp(["command_0x351635"]),
	SpriteSequence(sequence=3, identifier="command_0x351625"),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=20),
	PlaySound(sound=S0146_SLAP),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
	PlaySound(sound=S0146_SLAP),
	PauseScriptUntilSpriteSequenceDone(),
	ResetSpriteSequence(),
	RunSubroutine(["command_0x3523c4"], identifier="command_0x351635"),
	RunSubroutine(["command_0x35789e"]),
	ReturnSubroutine()
])
