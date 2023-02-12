# ChainSaw

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	Pause1Frame(),
	Pause1Frame(),
	Pause1Frame(),
	RunSubroutine(["command_0x3536eb"]),
	SetAMEM16BitToConst(0x60, 33),
	RunSubroutine(["command_0x35247f"]),
	Db(bytearray(b'\x8c')),
	Pause1Frame(),
	ReturnSubroutine()
])
