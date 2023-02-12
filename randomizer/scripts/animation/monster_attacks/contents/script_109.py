# Vigorup

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	SetOMEM60To072C(),
	DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
	RunSubroutine(["command_0x357b73"]),
	RunSubroutine(["command_0x353148"]),
	PlaySound(sound=S0092_SPEAR_RAIN_SINGLE),
	SetAMEM16BitToConst(0x60, 16),
	RunSubroutine(["command_0x35249d"]),
	RunSubroutine(["command_0x3577f2"]),
	ReturnSubroutine()
])
