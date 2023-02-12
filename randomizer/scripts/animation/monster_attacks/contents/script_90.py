# PhysicalAttack101

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	PlaySound(sound=S0004_JUMP),
	RunSubroutine(["command_0x357c7d"]),
	PlaySound(sound=S0018_SUPER_JUMP_HIT_1),
	RunSubroutine(["command_0x3523c4"]),
	RunSubroutine(["command_0x357cc3"]),
	ReturnSubroutine()
])
