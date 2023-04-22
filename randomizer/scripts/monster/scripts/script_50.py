"""50 - Clerk"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE004, [0]),
        IfLastMonsterStanding(),
        SetVarBits(0x7EE004, [0]),
        SetTarget(SELF),
        Attack(ValorUp),
        SetTarget(SELF),
        Attack(Vigorup),
        SetTarget(RANDOM_OPPONENT),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack1, PhysicalAttack1, PhysicalAttack25),
        StartCounterCommands(),
    ]
)
