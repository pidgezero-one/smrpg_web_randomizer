"""104 - Strawhead"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack3, PhysicalAttack3, Stench),
        Wait1Turn(),
        Attack(PhysicalAttack3, DarkClaw, ScrowFunk),
        Wait1Turn(),
        Attack(PhysicalAttack3, PhysicalAttack3, MushFunk),
        Wait1Turn(),
        StartCounterCommands(),
        IfTargetedByItem([PureWater]),
        IfTargetAlive(SELF),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
