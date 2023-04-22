"""84 - GlumReaper"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        Attack(PhysicalAttack5, Scythe, Deathsickle),
        Wait1TurnandRestartScript(),
        CastSpell(WillyWisp, LightningOrb, DrainBeam),
        StartCounterCommands(),
        IfTargetedByItem([PureWater]),
        IfTargetAlive(SELF),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
