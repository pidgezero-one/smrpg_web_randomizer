# 114 - Director

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfVarBitsClear(0x7EE004, [0]),
	IfLastMonsterStanding(),
	SetVarBits(0x7EE004, [0]),
	SetTarget(SELF),
	Attack(ValorUp),
	SetTarget(SELF),
	Attack(Vigorup),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	IfLastMonsterStanding(),
	CallTarget(MONSTER_2_CALL),
	CallTarget(MONSTER_3_CALL),
	CallTarget(MONSTER_4_CALL),
	CallTarget(MONSTER_5_CALL),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack1, PhysicalAttack25, SpritzBomb),
	StartCounterCommands(),
	IfTargetedByRegularAttack(),
	Attack(PhysicalAttack1, AttackDoNothing, AttackDoNothing),
	Wait1TurnandRestartScript()
])
