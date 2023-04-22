"""130 - BandanaRedHenchman"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfLastMonsterStanding(),
        SetTarget(SELF),
        CastSpell(Escape),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack1, PhysicalAttack1, Skewer),
        StartCounterCommands(),
    ]
)
