# PhysicalAttack7

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	PlaySound(sound=S0169_TELEPORT_ATTACK),
	RunSubroutine(["command_0x3578f1"]),
	RunSubroutine(["command_0x353140"]),
	RunSubroutine(["command_0x3523c4"]),
	RunSubroutine(["command_0x3577f2"]),
	ReturnSubroutine()
])
