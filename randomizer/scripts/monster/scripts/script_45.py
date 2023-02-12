# 45 - Shadow

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack5),
        Wait1Turn(),
        Attack(Endobubble),
        Wait1Turn(),
        Attack(PhysicalAttack5),
        Wait1Turn(),
        Attack(PhysicalAttack31),
        Wait1Turn(),
        StartCounterCommands(),
        IfTargetedByItem([PureWater]),
        IfTargetAlive(SELF),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
