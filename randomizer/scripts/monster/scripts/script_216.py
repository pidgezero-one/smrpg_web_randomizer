# 216 - KingCalamari

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 5),
	SetVarBits(0x7EE00F, [0]),
	Attack(PhysicalAttack0, InkBlast, VenomDrool),
	ClearVarBits(0x7EE00F, [0]),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Wait1TurnandRestartScript(),
	CastSpell(SandStorm, DrainBeam, DrainBeam),
	StartCounterCommands(),
	IfHPBelow(0),
	DoMonsterBehaviour(3),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])
