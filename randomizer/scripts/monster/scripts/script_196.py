# 196 - Jinx2

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE000, [0]),
        SetVarBits(0x7EE000, [0]),
        Attack(Quicksilver),
        Wait1TurnandRestartScript(),
        IfHPBelow(400, identifier="jinx2_def"),
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        SetTarget(SELF),
        Attack(ValorUp),
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
        Attack(Jinxed, TripleKick, Quicksilver),
        StartCounterCommands(),
        IfHPBelow(0),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfTargetedByRegularAttack(),
        Attack(TripleKick, AttackDoNothing, AttackDoNothing),
        Wait1TurnandRestartScript(),
    ]
)
