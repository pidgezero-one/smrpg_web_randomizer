# AuroraFlash

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x3536f8"]),
	RunSubroutine(["command_0x35252b"]),
	RunSubroutine(["command_0x3536eb"]),
	PlaySound(sound=S0020_AURORA_FLASH),
	SetAMEM16BitToConst(0x60, 18),
	RunSubroutine(["command_0x352475"]),
	Db(bytearray(b'\x8c')),
	RunSubroutine(["command_0x3536ff"]),
	ReturnSubroutine()
])
