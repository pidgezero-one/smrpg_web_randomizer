# 127 - Piledriver

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Attack(PhysicalAttack0, PhysicalAttack0, PhysicalAttack47),
	StartCounterCommands(),
	IfTargetedByCommand([COMMAND_ATTACK]),
	Attack(AttackDoNothing, AttackDoNothing, FearRoulette),
	Wait1TurnandRestartScript()
])
