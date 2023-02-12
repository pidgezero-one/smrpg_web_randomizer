# Blazer

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x357b73"]),
	RunSubroutine(["command_0x352523"]),
	SetAMEM16BitToConst(0x60, 2),
	RunSubroutine(["command_0x3524b1"]),
	RunSubroutine(["command_0x3577f2"]),
	RunSubroutine(["command_0x3523c4"]),
	ReturnSubroutine()
])
