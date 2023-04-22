"""109 - Doppel"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack5, PhysicalAttack5, Echofinder),
        Wait1Turn(),
        Attack(PhysicalAttack5, PhysicalAttack5, Endobubble),
        StartCounterCommands(),
        IfTargetedByItem([PureWater]),
        IfTargetAlive(SELF),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
