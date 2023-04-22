"""179 - Jagger"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(Terrapunch, PhysicalAttack98, PhysicalAttack98),
        Wait1Turn(),
        Attack(Terrapunch, PhysicalAttack98, PhysicalAttack98),
        Wait1Turn(),
        Attack(Terrapunch),
        StartCounterCommands(),
        IfHPBelow(0),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfTargetedByRegularAttack(),
        Attack(Terrapunch, AttackDoNothing, AttackDoNothing),
        Wait1TurnandRestartScript(),
    ]
)
