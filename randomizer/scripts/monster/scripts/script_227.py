"""227 - DrillBit"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(AttackDoNothing, PhysicalAttack1, Skewer),
        IncreaseVarBy1(0x7EE003),
        Wait1Turn(),
        Attack(AttackDoNothing, PhysicalAttack1, PhysicalAttack1),
        IncreaseVarBy1(0x7EE003),
        Wait1Turn(),
        StartCounterCommands(),
    ]
)
