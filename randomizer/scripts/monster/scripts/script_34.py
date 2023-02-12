# 34 - Leuko

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	CastSpell(Bolt, Bolt, StaticE),
	StartCounterCommands(),
	IfTargetedByCommand([COMMAND_SPECIAL]),
	CastSpell(Solidify),
	Wait1TurnandRestartScript()
])
