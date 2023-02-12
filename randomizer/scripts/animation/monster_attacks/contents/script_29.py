# DoomReverb

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x357b73"]),
	RunSubroutine(["command_0x35313b"]),
	PlaySound(sound=S0111_SLEDGE),
	SetAMEM16BitToConst(0x60, 4),
	RunSubroutine(["command_0x352475"]),
	RunSubroutine(["command_0x3577f2"]),
	PlaySound(sound=S0012_BOMB_EXPLOSION),
	RunSubroutine(["command_0x3523df"]),
	ReturnSubroutine()
])
