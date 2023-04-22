"""6 - Goomba"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack3),
        Wait1Turn(),
        Attack(PhysicalAttack3, PhysicalAttack16, PhysicalAttack3),
        Wait1Turn(),
        Attack(PhysicalAttack3),
        Wait1Turn(),
        StartCounterCommands(),
    ]
)
