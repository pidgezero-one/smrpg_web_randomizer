# 54 - Snapdragon

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	SetVarBits(0x7EE00F, [0]),
	Attack(PhysicalAttack4),
	ClearVarBits(0x7EE00F, [0]),
	StartCounterCommands(),
	IfTargetedByCommand([COMMAND_ATTACK]),
	Attack(AttackDoNothing, AttackDoNothing, PollenNap),
	Wait1TurnandRestartScript()
])
