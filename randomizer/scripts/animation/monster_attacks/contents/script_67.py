# Deathsickle

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x3577e2"]),
	RunSubroutine(["command_0x352523"]),
	PlaySound(sound=S0123_CHOMP_BITE),
	RunSubroutine(["command_0x3577f2"]),
	RunSubroutine(["command_0x3523c4"]),
	ReturnSubroutine()
])
