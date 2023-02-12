# 142 - Torte

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfVarBitsClear(0x7EE001, [0]),
	SetVarBits(0x7EE001, [0]),
	IfCurrentlyInFormationID(298),
	SetUntargetable(MONSTER_2_SET),
	MakeInvulnerable(MONSTER_3_SET),
	MakeInvulnerable(MONSTER_4_SET),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	RunBattleDialog(135),
	Attack(PhysicalAttack3),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	RunBattleDialog(136),
	Attack(PhysicalAttack3),
	StartCounterCommands()
])
