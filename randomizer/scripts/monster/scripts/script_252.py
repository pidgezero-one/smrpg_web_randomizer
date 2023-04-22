"""252 - Cloaker2"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsSet(0x7EE004, [0]),
        DoMonsterBehaviour(28),
        Wait1TurnandRestartScript(),
        SetVarBits(0x7EE00F, [0]),
        Attack(PhysicalAttack0, PhysicalAttack0, PhysicalAttack20),
        ClearVarBits(0x7EE00F, [0]),
        StartCounterCommands(),
        IfHPBelow(0),
        SetVarBits(0x7EE004, [0]),
        DoMonsterBehaviour(28),
        SetUntargetable(SELF),
        Wait1TurnandRestartScript(),
    ]
)
