# Backfire

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	SetAMEM8BitTo7E1x(0x6F, 0x7EE00F),
	JmpIfAMEM8BitEqualsConst(0x6F, 1, ["command_0x351a6c"]),
	RunSubroutine(["command_0x357b83"]),
	RunSubroutine(["command_0x3536f8"], identifier="command_0x351a6c"),
	RunSubroutine(["command_0x352523"]),
	SetAMEM16BitToConst(0x60, 34),
	RunSubroutine(["command_0x352475"]),
	RunSubroutine(["command_0x3577f2"]),
	RunSubroutine(["command_0x352439"]),
	RunSubroutine(["command_0x3536ff"]),
	ReturnSubroutine()
])
