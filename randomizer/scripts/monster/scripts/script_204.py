# 204 - Megasmilax

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfVarBitsClear(PARTY_SIZE, [0]),
	SetVarBits(PARTY_SIZE, [0]),
	CastSpell(PetalBlast),
	Wait1TurnandRestartScript(),
	IfTurnCounterEquals(4),
	CastSpell(PetalBlast),
	ClearVar(ATTACK_PHASE_COUNTER),
	Wait1TurnandRestartScript(),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	SetVarBits(0x7EE00F, [0]),
	Attack(PhysicalAttack0, PhysicalAttack0, ScrowDust),
	ClearVarBits(0x7EE00F, [0]),
	Wait1TurnandRestartScript(),
	CastSpell(Drain, FlameWall, FlameWall),
	StartCounterCommands(),
	IfHPBelow(0),
	DoMonsterBehaviour(3),
	IncreaseVarBy1(0x7EE00E),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByCommand([COMMAND_ATTACK]),
	SetVarBits(0x7EE00F, [0]),
	Attack(PhysicalAttack0, AttackDoNothing, AttackDoNothing),
	ClearVarBits(0x7EE00F, [0]),
	Wait1TurnandRestartScript()
])
