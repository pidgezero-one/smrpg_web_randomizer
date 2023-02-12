# IronMaiden

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	SetAMEM8BitTo7E1x(0x6F, 0x7EE00F),
	JmpIfAMEM8BitEqualsConst(0x6F, 1, ["command_0x351aff"]),
	RunSubroutine(["command_0x357b73"]),
	RunSubroutine(["command_0x352523"], identifier="command_0x351aff"),
	PlaySound(sound=S0141_LULLABY_MARIO_THEME),
	SetAMEM16BitToConst(0x60, 15),
	RunSubroutine(["command_0x35247f"]),
	RunSubroutine(["command_0x3577f2"]),
	RunSubroutine(["command_0x352439"]),
	ReturnSubroutine()
])
