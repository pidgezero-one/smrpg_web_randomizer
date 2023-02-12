# Sporocyst

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x357b73"]),
	RunSubroutine(["command_0x353148"]),
	PlaySound(sound=S0143_TOSS),
	SetAMEM16BitToConst(0x60, 16),
	RunSubroutine(["command_0x352475"]),
	RunSubroutine(["command_0x3577f2"]),
	ReturnSubroutine()
])
