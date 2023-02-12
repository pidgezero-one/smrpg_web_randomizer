# PhysicalAttack31

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x357b83"]),
	RunSubroutine(["command_0x353148"]),
	PlaySound(sound=S0086_LONG_FALL),
	SetAMEM16BitToConst(0x60, 16),
	RunSubroutine(["command_0x35247f"]),
	RunSubroutine(["command_0x3577f2"]),
	PlaySound(sound=S0012_BOMB_EXPLOSION),
	RunSubroutine(["command_0x3523df"]),
	ReturnSubroutine()
])
