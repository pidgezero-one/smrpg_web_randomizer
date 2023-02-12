# 65 - Spikester

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Attack(PhysicalAttack3),
	Wait1Turn(),
	Attack(Thornet, PhysicalAttack3, Funguspike),
	Wait1Turn(),
	StartCounterCommands()
])
