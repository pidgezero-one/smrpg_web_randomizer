# Shaker

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x357e6c"]),
	RunSubroutine(["command_0x353148"]),
	PlaySound(sound=S0092_SPEAR_RAIN_SINGLE),
	SetAMEM16BitToConst(0x60, 16),
	RunSubroutine(["command_0x3524b1"]),
	RunSubroutine(["command_0x357e1a"]),
	ReturnSubroutine()
])
