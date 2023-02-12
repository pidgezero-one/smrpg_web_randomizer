# 62 - Mastadoom

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        Attack(PhysicalAttack0, PhysicalAttack0, PhysicalAttack57),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Wait1TurnandRestartScript(),
        CastSpell(DrainBeam, Blizzard, DrainBeam),
        StartCounterCommands(),
        IfTargetedByItem([PureWater]),
        IfTargetAlive(SELF),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
