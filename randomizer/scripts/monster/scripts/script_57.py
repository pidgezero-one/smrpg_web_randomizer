# 57 - Jester

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 2),
	CastSpell(FlameStone),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack3, FullHouse, WildCard),
	StartCounterCommands()
])
