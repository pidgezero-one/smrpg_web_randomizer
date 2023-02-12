# 159 - Kinklink

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfVarBitsClear(0x7EE000, [0]),
	SetUntargetable(MONSTER_2_SET),
	SetVarBits(0x7EE000, [0]),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfHPBelow(0),
	SetTargetable(MONSTER_1_SET),
	SetTargetable(MONSTER_2_SET),
	RunBattleEvent(BE0001_UNUSED),
	ExitBattle(),
	Wait1TurnandRestartScript()
])
