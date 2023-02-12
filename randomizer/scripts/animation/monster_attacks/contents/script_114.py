

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x353437"]),
	SetOMEM60To072C(),
	DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
	SetAMEM16BitToConst(0x60, 4),
	ObjectQueueAtOffsetAndIndex(index=6, target_address=0x353706),
	RunSubroutine(["command_0x3533df"]),
	RunSubroutine(["command_0x357e88"]),
	PlaySound(sound=S0012_BOMB_EXPLOSION),
	RunSubroutine(["command_0x3533f5"]),
	RunSubroutine(["command_0x3523df"]),
	RunSubroutine(["command_0x3577f2"]),
	ReturnSubroutine()
])
