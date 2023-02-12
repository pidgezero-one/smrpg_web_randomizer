# 160 - BirdyHenchman

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfVarBitsSet(0x7EE004, [0]),
	RunBattleDialog(209),
	SetTarget(RANDOM_ALLY_OR_SELF),
	Attack(PhysicalAttack0),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack10, PhysicalAttack10, Grinder),
	StartCounterCommands(),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarBitsClear(0x7EE004, [0]),
	IfTargetedByCommand([COMMAND_SPECIAL]),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	RunBattleDialog(208),
	SetVarBits(0x7EE004, [0]),
	Wait1TurnandRestartScript()
])
