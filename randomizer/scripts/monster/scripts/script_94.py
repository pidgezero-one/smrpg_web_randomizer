# 94 - Geckit

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	RunBattleDialog(209),
	SetTarget(RANDOM_ALLY_OR_SELF),
	Attack(PhysicalAttack0),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack1, PhysicalAttack1, SleepSauce),
	StartCounterCommands()
])
