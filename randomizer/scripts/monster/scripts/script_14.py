# 14 - Pinwheel

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 6),
	Attack(PhysicalAttack1),
	Wait1TurnandRestartScript(),
	CastSpell(StaticE, StaticE, LightningOrb),
	StartCounterCommands()
])
