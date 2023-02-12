# 15 - Ratfunk

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 6),
	SetVarBits(0x7EE00F, [0]),
	Attack(PhysicalAttack6, PhysicalAttack6, Poison),
	ClearVarBits(0x7EE00F, [0]),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	SetTarget(SELF),
	CastSpell(Escape),
	StartCounterCommands()
])
