# 41 - Reacher

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfLastMonsterStanding(),
        Attack(PhysicalAttack0, PhysicalAttack57, PhysicalAttack56),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack0, PhysicalAttack0, Elegy),
        StartCounterCommands(),
        IfTargetedByItem([PureWater]),
        IfTargetAlive(SELF),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
