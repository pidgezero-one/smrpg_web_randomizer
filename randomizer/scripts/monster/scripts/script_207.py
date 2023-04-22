"""207 - AxemYellow"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsSet(0x7EE003, [3]),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack2, PhysicalAttack2, PhysicalAttack40),
        StartCounterCommands(),
        IfCurrentlyInFormationID(304),
        IfHPBelow(0),
        IfVarEqualOrGreaterThan(0x7EE00F, 4),
        SetUntargetable(SELF),
        SetTargetable(MONSTER_1_SET),
        SetVarBits(0x7EE003, [3]),
        SetVarBits(0x7EE002, [0]),
        RunBattleEvent(BE0067_AXEM_RANGERS_GROUP_FORMATION),
        Wait1TurnandRestartScript(),
        IfCurrentlyInFormationID(304),
        IfHPBelow(0),
        IncreaseVarBy1(0x7EE00F),
        SetUntargetable(SELF),
        SetVarBits(0x7EE003, [3]),
        RunBattleEvent(BE0065_UNUSED),
        Wait1TurnandRestartScript(),
        IfTargetedByCommand([COMMAND_ATTACK]),
        Attack(BodySlam),
        Wait1TurnandRestartScript(),
    ]
)
