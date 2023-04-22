"""217 - TentaclesLeft"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack0),
        IncreaseVarBy1(0x7EE009),
        Wait1TurnandRestartScript(),
        StartCounterCommands(),
        IfHPBelow(0),
        IfVarBitsSet(0x7EE003, [0]),
        IfVarBitsClear(0x7EE003, [1]),
        IncreaseVarBy1(0x7EE000),
        IfVarEqualOrGreaterThan(0x7EE000, 6),
        SetVarBits(0x7EE003, [1]),
        DoMonsterBehaviour(3),
        SetVarBits(0x7EE00D, [0]),
        DoMonsterBehaviour(2),
        ClearVar(0x7EE009),
        RunBattleEvent(BE0028_BEAT_TENTACLES_MOVE_ON_TO_KING_CALAMARI),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfHPBelow(0),
        IfVarBitsClear(0x7EE003, [0]),
        IncreaseVarBy1(0x7EE000),
        IfVarEqualOrGreaterThan(0x7EE000, 3),
        SetVarBits(0x7EE003, [0]),
        DoMonsterBehaviour(3),
        SetVarBits(0x7EE00D, [0]),
        DoMonsterBehaviour(2),
        ClearVar(0x7EE009),
        RunBattleEvent(BE0027_BEAT_TENTACLES_MOVE_ON_TO_NEXT),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfHPBelow(0),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
