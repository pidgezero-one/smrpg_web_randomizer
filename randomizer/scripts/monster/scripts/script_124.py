# 124 - Radish

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Attack(PhysicalAttack2, PhysicalAttack2, PhysicalAttack40),
	StartCounterCommands(),
	IfTargetedByCommand([COMMAND_ATTACK]),
	Attack(AttackDoNothing, AttackDoNothing, Endobubble),
	Wait1TurnandRestartScript()
])
