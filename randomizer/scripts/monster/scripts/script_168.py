"""168 - MachineMadeAxemRed"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        SetTarget(SELF),
        Attack(ValorUp),
        SetTarget(RANDOM_OPPONENT),
        Wait1TurnandRestartScript(),
        IfVarBitsClear(0x7EE004, [1]),
        SetVarBits(0x7EE004, [1]),
        SetTarget(SELF),
        Attack(Vigorup),
        SetTarget(RANDOM_OPPONENT),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack1, PhysicalAttack1, PhysicalAttack31),
        StartCounterCommands(),
    ]
)
