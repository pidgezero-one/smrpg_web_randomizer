# 26 - Spookum

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	CastSpell(Crystal, Drain, Drain),
	Wait1Turn(),
	Attack(PhysicalAttack3, PhysicalAttack3, GunkBall),
	Wait1Turn(),
	StartCounterCommands(),
	IfTargetedBySpell([Terrorize]),
	SetTarget(SELF),
	CastSpell(Escape),
	Wait1TurnandRestartScript()
])
