"""111 - Bobomb"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack85),
        RemoveTarget(SELF),
        StartCounterCommands(),
        IfHPBelow(0),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfTargetedByElement([Element.FIRE]),
        Attack(PhysicalAttack85),
        IncreaseVarBy1(0x7EE001),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
