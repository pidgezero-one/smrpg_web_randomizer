# 195 - Jinx1

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfHPBelow(300, identifier="jinx1_def"),
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        SetTarget(SELF),
        Attack(ValorUp),
        SetTarget(RANDOM_OPPONENT),
        Wait1TurnandRestartScript(),
        Attack(Jinxed, Jinxed, TripleKick),
        StartCounterCommands(),
        IfHPBelow(0),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfTargetedByRegularAttack(),
        Attack(Jinxed, AttackDoNothing, AttackDoNothing),
        Wait1TurnandRestartScript(),
    ]
)
