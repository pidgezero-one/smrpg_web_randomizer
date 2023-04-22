"""131 - PiranhaPlantHenchman"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack4, PhysicalAttack4, ScrowDust),
        Wait1Turn(),
        Attack(PhysicalAttack4, PhysicalAttack4, PollenNap),
        Wait1Turn(),
        StartCounterCommands(),
    ]
)
