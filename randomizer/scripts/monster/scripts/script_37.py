# 37 - Blaster

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfTurnCounterEquals(3),
	Attack(Blazer),
	ClearVar(ATTACK_PHASE_COUNTER),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack29, PhysicalAttack29, AttackDoNothing),
	StartCounterCommands()
])
