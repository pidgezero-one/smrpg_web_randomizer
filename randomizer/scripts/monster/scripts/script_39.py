# 39 - Babayaga

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsSet(0x7EE004, [0]),
        SetTarget(SELF),
        Attack(Thornet),
        ClearVarBits(0x7EE004, [0]),
        SetVarBits(0x7EE004, [1]),
        Wait1TurnandRestartScript(),
        IfTargetAlive(ALL_ALLIES_EXCLUDING_SELF),
        Attack(PhysicalAttack1, PhysicalAttack1, VenomDrool),
        Wait1TurnandRestartScript(),
        IfVarBitsSet(0x7EE004, [1]),
        CastSpell(SandStorm, MegaRecover, SandStorm),
        Wait1TurnandRestartScript(),
        SetVarBits(0x7EE004, [0]),
        Attack(PhysicalAttack1),
        StartCounterCommands(),
    ]
)
