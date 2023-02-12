# 129 - ApprenticeHenchman

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(StaticE, Bolt, Bolt),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack3, PhysicalAttack29, GunkBall),
	StartCounterCommands(),
	IfTargetKOed(),
	IncreaseVarBy1(0x7EE000),
	IfVarEqualOrGreaterThan(0x7EE000, 3),
	SetTargetable(MONSTER_1_SET),
	RunBattleDialog(69),
	Wait1TurnandRestartScript()
])
