# 63 - Corkpedite

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfTargetKOed(),
	DoMonsterBehaviour(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 2),
	CastSpell(SandStorm),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack0),
	StartCounterCommands()
])
