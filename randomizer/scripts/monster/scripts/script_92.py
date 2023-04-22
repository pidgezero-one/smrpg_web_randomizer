"""92 - Stinger"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfTurnCounterEquals(3),
        SetTarget(SELF),
        CastSpell(Escape),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack10, Thornet, Funguspike),
        StartCounterCommands(),
    ]
)
