"""81 - Magmus"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        SetTarget(SELF),
        Attack(ValorUp),
        SetTarget(RANDOM_OPPONENT),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack15),
        StartCounterCommands(),
    ]
)
