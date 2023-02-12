# 126 - MastaBlasta

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfHPBelow(512),
	CastSpell(Crystal, Blast, Storm),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack0, PhysicalAttack0, EerieJig),
	StartCounterCommands()
])
