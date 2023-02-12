# 212 - KingBomb

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfTurnCounterEquals(3),
	SetTargetable(MONSTER_1_SET),
	CastSpell(BigBang),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	StartCounterCommands(),
	IfHPBelow(0),
	ClearVar(0x7EE000),
	SetTargetable(MONSTER_1_SET),
	DoMonsterBehaviour(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])
