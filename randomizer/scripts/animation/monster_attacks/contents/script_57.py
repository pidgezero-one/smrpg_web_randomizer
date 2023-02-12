# Scream

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x357b73"]),
	PlaySound(sound=S0037_MONSTER_ITEM_TOSS),
	SetAMEM16BitToConst(0x60, 6),
	RunSubroutine(["command_0x35249d"]),
	RunSubroutine(["command_0x3577f2"]),
	ReturnSubroutine()
])
