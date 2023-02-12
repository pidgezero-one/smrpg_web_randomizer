# 243 - Earthlink

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	SetVarBits(0x7EE00F, [0]),
	Attack(PhysicalAttack0, Poison, CarniKiss),
	ClearVarBits(0x7EE00F, [0]),
	StartCounterCommands(),
	IfHPBelow(0),
	SetTargetable(MONSTER_1_SET),
	SetUntargetable(SELF),
	RunBattleEvent(BE0100_EARTHLINK_MAD_ADDER_COLLAPSES_AND_DIES),
	RemoveTarget(ALL_ALLIES_EXCLUDING_SELF),
	Wait1TurnandRestartScript()
])
