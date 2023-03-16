# 72 - Fireball

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 3),
        CastSpell(Drain, MegaDrain, Drain),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack2, PhysicalAttack2, PhysicalAttack2),
        StartCounterCommands(),
        IfTargetedByElement([Element.ICE]),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
