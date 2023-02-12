# 223 - MadAdder

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 5),
	CastSpell(SandStorm, Storm, WaterBlast),
	Wait1TurnandRestartScript(),
	CastSpell(SpellDoNothing, Boulder, Boulder),
	StartCounterCommands(),
	IfHPBelow(0),
	SetTargetable(MONSTER_2_SET),
	SetUntargetable(SELF),
	RunBattleEvent(BE0100_EARTHLINK_MAD_ADDER_COLLAPSES_AND_DIES),
	RemoveTarget(ALL_ALLIES_EXCLUDING_SELF),
	Wait1TurnandRestartScript()
])
