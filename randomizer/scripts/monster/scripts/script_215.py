# 215 - Raspberry

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfVarBitsClear(0x7EE000, [0]),
	Wait1TurnandRestartScript(),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(SandStorm, DrainBeam, SandStorm),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	SetVarBits(0x7EE00F, [0]),
	Attack(PhysicalAttack0, PhysicalAttack0, PhysicalAttack31),
	ClearVarBits(0x7EE00F, [0]),
	StartCounterCommands(),
	IfHPBelow(0),
	DoMonsterBehaviour(6),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])
