# 144 - JinxClone

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Attack(Jinxed, Jinxed, TripleKick),
	Wait1Turn(),
	Attack(Jinxed, TripleKick, Quicksilver),
	Wait1Turn(),
	Attack(Quicksilver, BombsAway, SilverBullet),
	Wait1Turn(),
	StartCounterCommands(),
	IfHPBelow(0),
	ClearVar(0x7EE000),
	SetTargetable(MONSTER_1_SET),
	DoMonsterBehaviour(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])
