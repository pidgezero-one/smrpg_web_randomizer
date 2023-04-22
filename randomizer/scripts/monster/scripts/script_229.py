"""229 - AxemBlack"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsSet(0x7EE003, [1]),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack5, PhysicalAttack5, PhysicalAttack25),
        IfTargetAlive(AT_LEAST_ONE_OPPONENT),
        Attack(PhysicalAttack5, PhysicalAttack5, PhysicalAttack25),
        Wait1TurnandRestartScript(),
        StartCounterCommands(),
        IfCurrentlyInFormationID(304),
        IfHPBelow(0),
        IfVarEqualOrGreaterThan(0x7EE00F, 4),
        SetUntargetable(SELF),
        SetTargetable(MONSTER_1_SET),
        SetVarBits(0x7EE003, [1]),
        SetVarBits(0x7EE002, [0]),
        RunBattleEvent(BE0067_AXEM_RANGERS_GROUP_FORMATION),
        Wait1TurnandRestartScript(),
        IfCurrentlyInFormationID(304),
        IfHPBelow(0),
        IncreaseVarBy1(0x7EE00F),
        SetUntargetable(SELF),
        SetVarBits(0x7EE003, [1]),
        RunBattleEvent(BE0064_UNUSED),
        Wait1TurnandRestartScript(),
        IfTargetedByCommand([COMMAND_SPECIAL]),
        Attack(SpritzBomb),
        Wait1TurnandRestartScript(),
    ]
)
