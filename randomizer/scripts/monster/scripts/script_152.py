# 152 - WindCrystal

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
	CastSpell(LightningOrb, Bolt, Electroshock),
	Wait1TurnandRestartScript(),
	CastSpell(StaticE, LightBeam, PetalBlast),
	StartCounterCommands()
])
