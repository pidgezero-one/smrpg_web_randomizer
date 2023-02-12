# 91 - Ninja

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 6),
	Attack(PhysicalAttack5, PhysicalAttack20, PhysicalAttack21),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	SetTarget(SELF),
	CastSpell(Escape),
	StartCounterCommands(),
	IfHPBelow(0),
	Attack(PhysicalAttack21),
	DoMonsterBehaviour(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])
