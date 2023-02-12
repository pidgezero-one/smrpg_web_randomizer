# 176 - Starslap

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Attack(PhysicalAttack2),
	Wait1Turn(),
	Attack(PhysicalAttack2),
	Wait1Turn(),
	SetTarget(RANDOM_ALLY_OR_SELF),
	CastSpell(Recover),
	SetTarget(RANDOM_OPPONENT),
	StartCounterCommands()
])
