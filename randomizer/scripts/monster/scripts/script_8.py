# 8 - Amanita

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Attack(PhysicalAttack3, PhysicalAttack3, Sporocyst),
	Wait1Turn(),
	Attack(PhysicalAttack3),
	StartCounterCommands(),
	IfTargetedByCommand([COMMAND_ATTACK]),
	Attack(PhysicalAttack3),
	Wait1TurnandRestartScript()
])
