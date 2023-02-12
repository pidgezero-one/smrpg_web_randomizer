# 53 - Remocon

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Attack(BodySlam, PhysicalAttack3, EerieJig),
	StartCounterCommands(),
	IfTargetedByRegularAttack(),
	IfTargetedByElement([SpellElement.Fire]),
	DoMonsterBehaviour(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])
