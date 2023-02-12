# PhysicalAttack93

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x357bb8"]),
	PlaySound(sound=S0012_BOMB_EXPLOSION),
	VisibilityOff(),
	SetAMEM16BitToConst(0x60, 11),
	RunSubroutine(["command_0x352475"]),
	RunSubroutine(["command_0x3523c4"]),
	ReturnSubroutine()
])
