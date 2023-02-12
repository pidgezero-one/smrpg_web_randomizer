# 218 - Jinx3

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE000, [0]),
        SetVarBits(0x7EE000, [0]),
        Attack(BombsAway),
        Wait1TurnandRestartScript(),
        IfHPBelow(600, identifier="jinx3_def_1"),
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        SetTarget(SELF),
        Attack(ValorUp),
        SetTarget(RANDOM_OPPONENT),
        Wait1TurnandRestartScript(),
        IfHPBelow(300, identifier="jinx3_def_2"),
        IfVarBitsClear(0x7EE004, [1]),
        SetVarBits(0x7EE004, [1]),
        SetVarBits(0x7EE00F, [0]),
        SetTarget(SELF),
        Attack(Vigorup),
        SetTarget(RANDOM_OPPONENT),
        Wait1TurnandRestartScript(),
        IfVarBitsClear(0x7EE004, [0]),
        Attack(Jinxed, TripleKick, Quicksilver),
        Wait1TurnandRestartScript(),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        Attack(SilverBullet),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Wait1TurnandRestartScript(),
        Attack(TripleKick, Quicksilver, BombsAway),
        StartCounterCommands(),
        IfHPBelow(0),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfTargetedByRegularAttack(),
        Attack(Quicksilver, AttackDoNothing, AttackDoNothing),
        Wait1TurnandRestartScript(),
    ]
)
