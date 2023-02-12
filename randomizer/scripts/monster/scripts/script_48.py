# 48 - Octolot

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 6),
	CastSpell(FlameWall, LightningOrb, Flame),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack2, GunkBall, PhysicalAttack2),
	StartCounterCommands()
])
