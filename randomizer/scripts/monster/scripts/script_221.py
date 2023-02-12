# 221 - Cloaker

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Attack(PhysicalAttack1, PhysicalAttack1, PhysicalAttack28),
	StartCounterCommands(),
	IfHPBelow(0),
	DoMonsterBehaviour(3),
	RunBattleEvent(BE0053_DOMINO_TEAMS_UP_WITH_MAD_ADDER),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])
