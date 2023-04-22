"""42 - Shogun"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack1, PhysicalAttack1, CarniKiss),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_SPECIAL]),
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        SetTarget(SELF),
        Attack(Vigorup),
        SetTarget(RANDOM_OPPONENT),
        Wait1TurnandRestartScript(),
    ]
)
