# 43 - Orbuser

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(Bolt, Flame, FlameWall),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	SetTarget(RANDOM_ALLY_OR_SELF),
	CastSpell(Recover),
	SetTarget(RANDOM_OPPONENT),
	StartCounterCommands()
])
