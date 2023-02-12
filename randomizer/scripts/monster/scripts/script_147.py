# 147 - Formless

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	CastSpell(Bolt, StaticE, Electroshock),
	Wait1Turn(),
	CastSpell(Bolt, Crystal, Solidify),
	StartCounterCommands(),
	IfTargetedByCommand([COMMAND_SPECIAL]),
	RunBattleDialog(214),
	RunBattleEvent(BE0075_FORMLESS_CHANGES_INTO_MOKURA),
	RemoveTarget(SELF),
	Wait1TurnandRestartScript()
])
