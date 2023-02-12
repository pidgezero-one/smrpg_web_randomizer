# 193 - GrateGuy

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfVarBitsSet(0x7EE000, [0]),
	CastSpell(MeteorBlast),
	IncreaseVarBy1(0x7EE002),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack1, Echofinder, PhysicalAttack51),
	IncreaseVarBy1(0x7EE002),
	StartCounterCommands(),
	IfHPBelow(0),
	IfLastMonsterStanding(),
	DoMonsterBehaviour(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	IfVarBitsSet(0x7EE000, [0]),
	ClearVarBits(0x7EE000, [0]),
	RunBattleEvent(BE0019_KNIFE_GUY_GRATE_GUY_SEPARATE_YIKES_THEY_RE_PRETTY_TOUGH),
	DoMonsterBehaviour(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfHPBelow(0),
	DoMonsterBehaviour(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	IncreaseVarBy1(0x7EE001),
	IfVarBitsSet(0x7EE000, [0]),
	IfVarEqualOrGreaterThan(0x7EE001, 5),
	ClearVarBits(0x7EE000, [0]),
	ClearVar(0x7EE002),
	RunBattleEvent(BE0019_KNIFE_GUY_GRATE_GUY_SEPARATE_YIKES_THEY_RE_PRETTY_TOUGH),
	Wait1TurnandRestartScript()
])
