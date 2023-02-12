# 205 - Birdo

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfVarEqualOrGreaterThan(0x7EE000, 3),
	IfVarBitsClear(0x7EE004, [0]),
	SetVarBits(0x7EE004, [0]),
	Attack(PhysicalAttack116),
	Wait1TurnandRestartScript(),
	IfVarBitsSet(0x7EE004, [0]),
	Attack(PhysicalAttack115, PhysicalAttack116, PhysicalAttack116),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack115),
	StartCounterCommands(),
	IfHPBelow(0),
	DoMonsterBehaviour(3),
	SetVarBits(0x7EE00F, [0]),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	IncreaseVarBy1(0x7EE000),
	Wait1TurnandRestartScript()
])
