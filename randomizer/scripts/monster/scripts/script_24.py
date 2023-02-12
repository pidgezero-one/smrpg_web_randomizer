# 24 - ShyRanger

from randomizer.scripts.monster.script_imports import *

script = MonsterScript([
	IfVarBitsClear(0x7EE004, [0]),
	SetTarget(SELF),
	CastSpell(Escape),
	Wait1TurnandRestartScript(),
	Attack(PhysicalAttack107, PhysicalAttack20, PhysicalAttack21),
	StartCounterCommands(),
	IfTargetAfflictedBy(SELF, [SpellStatusEffects.Mute, SpellStatusEffects.Sleep, SpellStatusEffects.Poison, SpellStatusEffects.Fear]),
	SetVarBits(0x7EE004, [0]),
	Wait1TurnandRestartScript(),
	IfTargetedByRegularAttack(),
	Attack(PhysicalAttack107, AttackDoNothing, AttackDoNothing),
	Wait1TurnandRestartScript()
])
