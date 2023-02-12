# 219 - Zombone

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfVarBitsClear(0x7EE004, [0]),
	SetVarBits(0x7EE004, [0]),
	CastSpell(Boulder),
	Wait1TurnandRestartScript(),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(Blast, Storm, Boulder),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack1, PhysicalAttack1, Scream),
	StartCounterCommands(),
	IfHPBelow(0),
	RunBattleEvent(BE0045_ZOMBONE_DIES),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByItem([PureWater]),
	SetTarget(SELF),
	Attack(PhysicalAttack0),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	Attack(PhysicalAttack1, AttackDoNothing, AttackDoNothing),
	Wait1TurnandRestartScript()
])
