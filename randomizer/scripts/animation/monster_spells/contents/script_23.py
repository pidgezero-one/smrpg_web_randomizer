# LightBeam

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x3536f8"]),
	RunSubroutine(["command_0x35252b"]),
	RunSubroutine(["command_0x3536eb"]),
	PlaySound(sound=S0106_LIGHT_BEAM),
	SetAMEM16BitToConst(0x60, 0),
	RunSubroutine(["command_0x3524a7"]),
	Db(bytearray(b'\x8c')),
	RunSubroutine(["command_0x3536ff"]),
	ReturnSubroutine()
])
