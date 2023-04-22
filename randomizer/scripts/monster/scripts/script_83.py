"""83 - Vomer"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack3, PhysicalAttack3, PhysicalAttack56),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_SPECIAL]),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfTargetedByItem([PureWater]),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
