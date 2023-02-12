# 153 - MarioClone

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Attack(PhysicalAttack90),
	StartCounterCommands(),
	IfHPBelow(0),
	IfVarBitsSet(0x7EE004, [0]),
	ClearVarBits(0x7EE00E, [1]),
	DecreaseVarBy1(0x7EE000),
	DoMonsterBehaviour(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	ClearVarBits(0x7EE00E, [0]),
	DecreaseVarBy1(0x7EE000),
	DoMonsterBehaviour(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByItem([PureWater]),
	IfTargetAlive(SELF),
	IfVarBitsSet(0x7EE004, [0]),
	ClearVarBits(0x7EE00E, [1]),
	DecreaseVarBy1(0x7EE000),
	DoMonsterBehaviour(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByItem([PureWater]),
	IfTargetAlive(SELF),
	ClearVarBits(0x7EE00E, [0]),
	DecreaseVarBy1(0x7EE000),
	DoMonsterBehaviour(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])
