# 40 - Hobgoblin

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack3, DarkClaw, Elegy),
        Wait1Turn(),
        Attack(PhysicalAttack3, DarkClaw, DarkClaw),
        Wait1Turn(),
        StartCounterCommands(),
        IfTargetedByItem([PureWater]),
        IfTargetAlive(SELF),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
