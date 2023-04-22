"""80 - Chow"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack1, PhysicalAttack1, Poison),
        Wait1Turn(),
        Attack(Howl),
        Wait1Turn(),
        Attack(PhysicalAttack1, PhysicalAttack1, Claw),
        Wait1Turn(),
        StartCounterCommands(),
    ]
)
