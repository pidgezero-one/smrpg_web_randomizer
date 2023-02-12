# 162 - Smelter

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfVarBitsSet(0x7EE004, [0]),
	Wait1TurnandRestartScript(),
	IfTurnCounterEquals(2),
	IfVarLessThan(0x7EE000, 2),
	SetVarBits(0x7EE003, [0]),
	ClearVar(ATTACK_PHASE_COUNTER),
	IncreaseVarBy1(0x7EE000),
	RunBattleEvent(BE0086_SMELTER_POURS_MOLTEN_LIQUID_SMITHY_WELDS),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfHPBelow(0),
	SetVarBits(0x7EE004, [0]),
	SetUntargetable(SELF),
	Wait1TurnandRestartScript()
])
