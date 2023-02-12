# Mushroom

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	Set7E1xToAMEM16Bit(0x7EE022, 0x60),
	RunSubroutine(["command_0x35caac"]),
	RunSubroutine(["command_0x35c968"]),
	ReturnSubroutine()
])
