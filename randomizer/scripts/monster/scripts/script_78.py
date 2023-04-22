"""78 - Bluebird"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 3),
        Attack(PhysicalAttack5, PhysicalAttack5, PhysicalAttack20),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Wait1TurnandRestartScript(),
        SetTarget(SELF),
        CastSpell(Escape),
        StartCounterCommands(),
    ]
)
