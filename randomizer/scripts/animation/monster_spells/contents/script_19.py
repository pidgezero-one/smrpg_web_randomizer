# SandStorm

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x35252b"]),
	RunSubroutine(["command_0x3536eb"]),
	PlaySound(sound=S0096_RUMBLE_MULTI),
	SetAMEM16BitToConst(0x60, 11),
	RunSubroutine(["command_0x352493"]),
	StopCurrentSoundEffect(),
	Db(bytearray(b'\x8c')),
	ReturnSubroutine()
])
