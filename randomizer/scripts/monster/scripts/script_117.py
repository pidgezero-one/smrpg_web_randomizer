# 117 - Puppox

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Attack(PhysicalAttack46, PhysicalAttack3, EerieJig),
	Wait1Turn(),
	Attack(PhysicalAttack46, PhysicalAttack3, SomnusWaltz),
	StartCounterCommands()
])
