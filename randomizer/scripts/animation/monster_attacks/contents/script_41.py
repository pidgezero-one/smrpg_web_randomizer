# PsychoPlasm

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x357b73"]),
	RunSubroutine(["command_0x352523"]),
	PlaySound(sound=S0097_PLASMA_TOSS),
	SetAMEM16BitToConst(0x60, 19),
	RunSubroutine(["command_0x352489"]),
	RunSubroutine(["command_0x3577f2"]),
	RunSubroutine(["command_0x352439"]),
	ReturnSubroutine()
])
