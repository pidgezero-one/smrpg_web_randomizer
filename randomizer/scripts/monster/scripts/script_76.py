# 76 - BandanaBlue

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfLastMonsterStanding(),
	CallTarget(MONSTER_2_CALL),
	CallTarget(MONSTER_3_CALL),
	CallTarget(MONSTER_4_CALL),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack1, PhysicalAttack25, SpritzBomb),
	StartCounterCommands(),
	IfTargetedByRegularAttack(),
	Attack(PhysicalAttack1, AttackDoNothing, AttackDoNothing),
	Wait1TurnandRestartScript()
])
