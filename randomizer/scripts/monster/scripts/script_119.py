"""119 - Lumbler"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack0, AttackDoNothing, AttackDoNothing),
        Wait1Turn(),
        Attack(PhysicalAttack0, AttackDoNothing, AttackDoNothing),
        Wait1Turn(),
        CastSpell(Crystal),
        Attack(PhysicalAttack115),
        Wait1Turn(),
        StartCounterCommands(),
    ]
)
