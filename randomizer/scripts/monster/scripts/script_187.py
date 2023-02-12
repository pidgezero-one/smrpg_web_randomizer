# 187 - Neosquid

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfVarBitsSet(0x7EE001, [0]),
	IfVarEqualOrGreaterThan(0x7EE004, 3),
	SetTargetable(SELF),
	ClearVar(0x7EE004),
	ClearVar(0x7EE001),
	DoMonsterBehaviour(13),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(0x7EE001, [0]),
	IncreaseVarBy1(0x7EE004),
	Wait1TurnandRestartScript(),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(Solidify, AuroraFlash, Corona),
	Wait1TurnandRestartScript(),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(StaticE, FlameWall, WaterBlast),
	Wait1TurnandRestartScript(),
	SetVarBits(0x7EE00F, [0]),
	Attack(PhysicalAttack0, CarniKiss, LullaBye),
	ClearVarBits(0x7EE00F, [0]),
	StartCounterCommands(),
	IfHPBelow(0),
	SetVarBits(0x7EE001, [0]),
	SetUntargetable(SELF),
	DoMonsterBehaviour(10),
	Wait1TurnandRestartScript()
])
