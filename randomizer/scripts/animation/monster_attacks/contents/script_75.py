# Psyche

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
	RunSubroutine(["command_0x3578f1"]),
	SetAMEM16BitToConst(0x60, 14),
	RunSubroutine(["command_0x3524df"]),
	RunSubroutine(["command_0x3577f2"]),
	PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
	RunSubroutine(["command_0x35242a"]),
	ReturnSubroutine()
])
