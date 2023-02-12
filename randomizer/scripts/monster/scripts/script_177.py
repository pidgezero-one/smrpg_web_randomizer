# 177 - Mukumuku

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Attack(PhysicalAttack111, PhysicalAttack111, PhysicalAttack113),
	Wait1Turn(),
	Attack(PhysicalAttack113, Missedme, PhysicalAttack113),
	Wait1Turn(),
	StartCounterCommands()
])
