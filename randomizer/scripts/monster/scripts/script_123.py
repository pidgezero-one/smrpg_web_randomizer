# 123 - Spinthra

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Attack(Poison, PhysicalAttack1, PhysicalAttack1),
	Wait1Turn(),
	Attack(PhysicalAttack1, PhysicalAttack1, ScrowFangs),
	Wait1Turn(),
	StartCounterCommands()
])
