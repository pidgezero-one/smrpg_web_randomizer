# 33 - Magikoopa

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfVarBitsSet(0x7EE000, [0]),
	Wait1TurnandRestartScript(),
	IfVarBitsClear(0x7EE000, [0]),
	IfVarEqualOrGreaterThan(0x7EE001, 1),
	ClearVar(0x7EE001),
	SetVarBits(0x7EE000, [0]),
	SetUntargetable(SELF),
	RunBattleEvent(BE0079_MAGIKOOPA_SUMMONS_MONSTER),
	RunBattleDialog(217),
	Wait1TurnandRestartScript(),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(Bolt, Blast, WillyWisp),
	IncreaseVarBy1(0x7EE001),
	Wait1TurnandRestartScript(),
	CastSpell(WaterBlast, Solidify, FlameWall),
	IncreaseVarBy1(0x7EE001),
	StartCounterCommands(),
	IfHPBelow(0),
	DoMonsterBehaviour(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])
