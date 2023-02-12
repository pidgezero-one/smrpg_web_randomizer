# 18 - TheBigBoo

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack12, PhysicalAttack12, Scream),
        Wait1Turn(),
        CastSpell(LightningOrb, LightningOrb, Bolt),
        Wait1Turn(),
        StartCounterCommands(),
        IfTargetedByItem([PureWater]),
        IfTargetAlive(SELF),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
