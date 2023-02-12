# WarFan

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	PlaySound(sound=S0160_SLAP),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=3),
	PlaySound(sound=S0160_SLAP),
	Jmp(["command_0x358251"])
])
