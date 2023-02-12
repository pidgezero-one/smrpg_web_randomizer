# 22 - Chomp

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Attack(PhysicalAttack0, IronMaiden, IronMaiden),
	Wait1Turn(),
	Attack(PhysicalAttack0),
	Wait1Turn(),
	Attack(CarniKiss),
	Wait1Turn(),
	StartCounterCommands()
])
