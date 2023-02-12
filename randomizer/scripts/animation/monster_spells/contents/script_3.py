# Bolt

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x3536f8"]),
	RunSubroutine(["command_0x35252b"]),
	PlaySound(sound=S0044_BOLT),
	SetAMEM16BitToConst(0x60, 17),
	RunSubroutine(["command_0x352475"]),
	RunSubroutine(["command_0x3536ff"]),
	ReturnSubroutine()
])
