"""184 - Microbomb"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack85, PhysicalAttack85, PhysicalAttack86),
        RemoveTarget(SELF),
        StartCounterCommands(),
        IfHPBelow(0),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfTargetedByElement([Element.FIRE]),
        Attack(PhysicalAttack85),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
