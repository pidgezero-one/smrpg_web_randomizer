# 228 - AxemPink

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfVarBitsSet(0x7EE003, [0]),
	Wait1TurnandRestartScript(),
	IfVarEqualOrGreaterThan(0x7EE00F, 1),
	IfVarBitsClear(0x7EE004, [0]),
	SetVarBits(0x7EE004, [0]),
	CastSpell(PetalBlast),
	Wait1TurnandRestartScript(),
	SetTarget(RANDOM_ALLY_OR_SELF),
	CastSpell(Recover, Recover, MegaRecover),
	SetTarget(RANDOM_OPPONENT),
	StartCounterCommands(),
	IfCurrentlyInFormationID(304),
	IfHPBelow(0),
	IfVarEqualOrGreaterThan(0x7EE00F, 4),
	SetUntargetable(SELF),
	SetTargetable(MONSTER_1_SET),
	SetVarBits(0x7EE003, [0]),
	SetVarBits(0x7EE002, [0]),
	RunBattleEvent(BE0067_AXEM_RANGERS_GROUP_FORMATION),
	Wait1TurnandRestartScript(),
	IfCurrentlyInFormationID(304),
	IfHPBelow(0),
	IncreaseVarBy1(0x7EE00F),
	SetUntargetable(SELF),
	SetVarBits(0x7EE003, [0]),
	RunBattleEvent(BE0063_UNUSED),
	Wait1TurnandRestartScript(),
	IfTargetedByCommand([COMMAND_SPECIAL]),
	SetTarget(RANDOM_OPPONENT),
	Attack(AttackDoNothing, PhysicalAttack3, PhysicalAttack51),
	Wait1TurnandRestartScript()
])
