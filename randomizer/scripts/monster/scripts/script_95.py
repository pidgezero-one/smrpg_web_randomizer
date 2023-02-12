# 95 - Jabit

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 3),
	Attack(PhysicalAttack1),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	Attack(LastShot),
	RemoveTarget(SELF),
	StartCounterCommands()
])
