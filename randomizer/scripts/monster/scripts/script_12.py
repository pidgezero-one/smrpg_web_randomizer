# 12 - Lakitu

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	Attack(PhysicalAttack1, PhysicalAttack1, Chomp),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	CastSpell(Bolt, Bolt, StaticE),
	StartCounterCommands()
])
