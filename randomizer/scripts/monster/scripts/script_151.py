# 151 - EarthCrystal

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfCurrentlyInFormationID(350),
	IfTargetKOed(),
	DoMonsterBehaviour(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(Blast, Blast, Storm),
	Wait1TurnandRestartScript(),
	CastSpell(SandStorm, WaterBlast, Boulder),
	StartCounterCommands()
])
