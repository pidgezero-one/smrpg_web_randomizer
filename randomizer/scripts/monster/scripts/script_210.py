"""210 - AxemRed"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsSet(0x7EE003, [2]),
        Wait1TurnandRestartScript(),
        IfVarEqualOrGreaterThan(0x7EE00F, 2),
        IfVarBitsClear(0x7EE004, [1]),
        SetVarBits(0x7EE004, [1]),
        SetTarget(SELF),
        Attack(Vigorup),
        SetTarget(RANDOM_OPPONENT),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack1, PhysicalAttack1, PhysicalAttack31),
        StartCounterCommands(),
        IfHPBelow(0),
        IfVarEqualOrGreaterThan(0x7EE00F, 4),
        SetUntargetable(SELF),
        SetTargetable(MONSTER_1_SET),
        SetVarBits(0x7EE003, [2]),
        SetVarBits(0x7EE002, [0]),
        RunBattleEvent(BE0067_AXEM_RANGERS_GROUP_FORMATION),
        Wait1TurnandRestartScript(),
        IfHPBelow(0),
        IncreaseVarBy1(0x7EE00F),
        SetUntargetable(SELF),
        SetVarBits(0x7EE003, [2]),
        RunBattleEvent(BE0068_UNUSED),
        Wait1TurnandRestartScript(),
    ]
)
