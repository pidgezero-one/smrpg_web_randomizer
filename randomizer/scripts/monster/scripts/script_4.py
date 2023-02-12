# 4 - Shaman

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(DiamondSaw, LightningOrb, Crystal),
	Wait1TurnandRestartScript(),
	ClearVar(DESIGNATED_RANDOM_NUM_VAR),
	Set7EE005ToRandomNumber(upper_bound=7),
	IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
	CastSpell(Blizzard, Blizzard, FlameStone),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack3),
	StartCounterCommands(),
	IfTargetedByCommand([COMMAND_SPECIAL]),
	SetTarget(SELF),
	CastSpell(Escape, SpellDoNothing, SpellDoNothing),
	SetTarget(RANDOM_OPPONENT),
	Wait1TurnandRestartScript()
])
