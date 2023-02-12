# 89 - Robomb

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 2),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack85, PhysicalAttack85, PhysicalAttack86),
	RemoveTarget(SELF),
	StartCounterCommands(),
	IfTargetedByElement([SpellElement.Fire]),
	Attack(PhysicalAttack85, PhysicalAttack85, PhysicalAttack86),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])
