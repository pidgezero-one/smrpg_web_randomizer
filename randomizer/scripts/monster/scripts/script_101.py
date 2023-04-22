"""101 - BigBertha"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack29),
        Wait1Turn(),
        Attack(PhysicalAttack29, PhysicalAttack29, Blazer),
        StartCounterCommands(),
    ]
)
