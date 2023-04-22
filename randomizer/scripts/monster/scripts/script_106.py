"""106 - ArmoredAnt"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE004, [0]),
        IfLastMonsterStanding(),
        SetVarBits(0x7EE004, [0]),
        SetTarget(SELF),
        Attack(Vigorup),
        SetTarget(RANDOM_OPPONENT),
        Attack(PhysicalAttack1),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack1, Endobubble, PhysicalAttack1),
        StartCounterCommands(),
    ]
)
