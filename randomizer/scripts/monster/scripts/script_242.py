# 242 - MachineMadeAxemYellowHenchman

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	Attack(PhysicalAttack2, PhysicalAttack2, PhysicalAttack40),
	StartCounterCommands(),
	IfTargetedByCommand([COMMAND_ATTACK]),
	Attack(BodySlam),
	Wait1TurnandRestartScript()
])
