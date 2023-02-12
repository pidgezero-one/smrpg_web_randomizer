# Fangs

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x357b73"]),
	RunSubroutine(["command_0x352523"]),
	PlaySound(sound=S0133_LULLABY_SAD_SONG),
	SetAMEM16BitToConst(0x60, 15),
	RunSubroutine(["command_0x35247f"]),
	RunSubroutine(["command_0x3577f2"]),
	RunSubroutine(["command_0x352448"]),
	ReturnSubroutine()
])
