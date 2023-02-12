# Parasol

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	PlaySound(sound=S0046_PLASMA_BOUNCE),
	Jmp(["command_0x358251"])
])
