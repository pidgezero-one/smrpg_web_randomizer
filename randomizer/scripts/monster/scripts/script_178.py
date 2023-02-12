# 178 - Zeostar

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Attack(PhysicalAttack2, PhysicalAttack2, ViroPlasm),
	StartCounterCommands(),
	IfTargetedByCommand([COMMAND_ATTACK]),
	SetTarget(RANDOM_ALLY_OR_SELF),
	CastSpell(Recover),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript()
])
