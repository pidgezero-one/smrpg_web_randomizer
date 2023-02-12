

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	SpriteSequence(sequence=3),
	PauseScriptUntilSpriteSequenceDone(),
	PlaySound(sound=S0051_FIRE_THROW_BIG),
	SetAMEM16BitToConst(0x60, 25),
	RunSubroutine(["command_0x352475"]),
	Jmp(["command_0x35346c"]),
	PlaySound(sound=S0084_WALLOP_4),
	RunSubroutine(["command_0x3523df"]),
	Jmp(["command_0x352016"]),
	AttackTimerBegins(),
	PlaySound(sound=S0054_HAMMER_HIT_1),
	ResetSpriteSequence(identifier="command_0x352016"),
	ReturnSubroutine()
])
