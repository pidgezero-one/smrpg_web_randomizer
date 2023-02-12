# LazyShellWeapon

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	PlaySound(sound=S0194_BIG_SHELL_HIT_2),
	Jmp(["command_0x358251"])
])
