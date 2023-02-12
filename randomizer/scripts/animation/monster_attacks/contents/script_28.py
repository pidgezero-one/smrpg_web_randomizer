# ScrowBell

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	RunSubroutine(["command_0x353148"]),
	PlaySound(sound=S0037_MONSTER_ITEM_TOSS),
	SetAMEM16BitToConst(0x60, 10),
	RunSubroutine(["command_0x352493"]),
	RunSubroutine(["command_0x3523c4"]),
	ReturnSubroutine()
])
