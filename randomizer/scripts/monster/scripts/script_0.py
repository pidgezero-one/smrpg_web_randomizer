"""0 - Terrapin"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(AttackDoNothing, PhysicalAttack98, PhysicalAttack98),
        StartCounterCommands(),
    ]
)
