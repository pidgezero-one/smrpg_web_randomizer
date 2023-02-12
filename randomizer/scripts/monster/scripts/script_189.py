# 189 - Helio

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Attack(PhysicalAttack117),
	RemoveTarget(SELF),
	StartCounterCommands()
])
