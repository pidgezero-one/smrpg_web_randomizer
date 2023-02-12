# FryingPan

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	PlaySound(sound=S0083_FRYING_PAN_HIT_1),
	Jmp(["command_0x358251"])
])
