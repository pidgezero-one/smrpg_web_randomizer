# 133 - MadMalletHenchman

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfLastMonsterStanding(),
	SetTarget(SELF),
	CastSpell(Escape),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack1),
	StartCounterCommands()
])
