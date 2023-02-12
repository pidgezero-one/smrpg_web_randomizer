# 27 - HammerBro

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfTargetAlive(ALL_ALLIES_EXCLUDING_SELF),
        SetTarget(RANDOM_OPPONENT),
        Attack(HammerTime, PhysicalAttack3, PhysicalAttack3),
        Wait1TurnandRestartScript(),
        IfVarBitsClear(0x7EE000, [0]),
        SetTarget(SELF),
        Attack(ValorUp),
        SetTarget(RANDOM_OPPONENT),
        SetVarBits(0x7EE000, [0]),
        Wait1TurnandRestartScript(),
        Attack(HammerTime, PhysicalAttack3, PhysicalAttack3),
        StartCounterCommands(),
        IfHPBelow(0),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
