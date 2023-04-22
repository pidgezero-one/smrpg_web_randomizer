"""74 - MrKipper"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack1, PhysicalAttack1, Thornet),
        Wait1Turn(),
        Attack(PhysicalAttack1, PhysicalAttack21, Funguspike),
        StartCounterCommands(),
    ]
)
