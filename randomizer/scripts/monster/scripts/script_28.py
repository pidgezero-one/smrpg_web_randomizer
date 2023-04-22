"""28 - Buzzer"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfLastMonsterStanding(),
        SetTarget(SELF),
        CastSpell(Escape),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack10, PhysicalAttack10, Thornet),
        StartCounterCommands(),
        IfTargetedByElement([Element.FIRE]),
        SetTarget(SELF),
        CastSpell(Escape),
        Wait1TurnandRestartScript(),
    ]
)
