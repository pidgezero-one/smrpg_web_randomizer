

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	SetOMEM60To072C(),
	DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
	RunSubroutine(["command_0x35313b"]),
	PlaySound(sound=S0122_POISONED),
	RunSubroutine(["command_0x3523c4"]),
	ReturnSubroutine()
])
