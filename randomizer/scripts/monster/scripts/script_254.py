# 254 - Candle

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfTurnCounterEquals(3),
	SetTargetable(SELF),
	ClearVar(ATTACK_PHASE_COUNTER),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfTargetedByRegularAttack(),
	SetUntargetable(SELF),
	Wait1TurnandRestartScript()
])
