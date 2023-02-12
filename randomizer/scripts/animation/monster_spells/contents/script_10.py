# Blast

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x35252b"]),
	PlaySound(sound=S0012_BOMB_EXPLOSION),
	SetAMEM16BitToConst(0x60, 29),
	RunSubroutine(["command_0x352475"]),
	ReturnSubroutine()
])
