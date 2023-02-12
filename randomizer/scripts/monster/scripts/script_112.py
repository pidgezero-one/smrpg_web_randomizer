# 112 - Octovader

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(LightningOrb, Bolt, DrainBeam),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack2, PhysicalAttack2, SleepSauce),
	StartCounterCommands(),
	IfTargetedByCommand([COMMAND_ATTACK]),
	Attack(AttackDoNothing, AttackDoNothing, GunkBall),
	Wait1TurnandRestartScript()
])
