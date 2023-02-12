# 148 - Mokura

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(Bolt, StaticE, Electroshock),
	Wait1TurnandRestartScript(),
	CastSpell(Bolt, Crystal, Solidify),
	StartCounterCommands()
])
