# Scythe

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x357b73"]),
	RunSubroutine(["command_0x352523"]),
	PlaySound(sound=S0108_HOWL),
	SetAMEM16BitToConst(0x60, 13),
	RunSubroutine(["command_0x352475"]),
	RunSubroutine(["command_0x3577f2"]),
	RunSubroutine(["command_0x35242a"]),
	ReturnSubroutine()
])
