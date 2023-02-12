# 30 - Gecko

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfLastMonsterStanding(),
	SetTarget(SELF),
	CastSpell(Escape),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack1, PhysicalAttack1, FunRun),
	Wait1Turn(),
	Attack(PhysicalAttack40, VenomDrool, SleepSauce),
	Wait1Turn(),
	StartCounterCommands()
])
