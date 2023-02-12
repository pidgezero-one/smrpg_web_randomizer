# WildCard

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x357b73"]),
	RunSubroutine(["command_0x353148"]),
	PlaySound(sound=S0125_SPIKE_SHOT),
	SetAMEM16BitToConst(0x60, 1),
	RunSubroutine(["command_0x352489"]),
	RunSubroutine(["command_0x3577f2"]),
	PlaySound(sound=S0015_SPIKE_STING),
	RunSubroutine(["command_0x3523c4"]),
	ReturnSubroutine()
])
