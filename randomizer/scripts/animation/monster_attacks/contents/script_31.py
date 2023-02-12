# InkBlast

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	SetAMEM8BitTo7E1x(0x6F, 0x7EE00F),
	JmpIfAMEM8BitEqualsConst(0x6F, 1, ["command_0x351831"]),
	RunSubroutine(["command_0x357b73"]),
	SetAMEM16BitToConst(0x60, 5, identifier="command_0x351831"),
	RunSubroutine(["command_0x35247f"]),
	RunSubroutine(["command_0x3577f2"]),
	RunSubroutine(["command_0x3523c4"]),
	ReturnSubroutine()
])
