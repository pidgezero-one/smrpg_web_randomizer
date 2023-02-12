# PhysicalAttack32

from randomizer.scripts.animation.script_imports import *

script = AnimationScript([
	DisplayMessageAtOMEM60As(BATTLE_DIALOGUE),
	RunSubroutine(["command_0x357c57"]),
	PlaySound(sound=S0111_SLEDGE),
	SetAMEM16BitToConst(0x60, 16),
	RunSubroutine(["command_0x352489"]),
	RunSubroutine(["command_0x3577f2"]),
	AttackTimerBegins(),
	ReturnSubroutine()
])
