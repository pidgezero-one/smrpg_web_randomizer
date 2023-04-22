"""143 - Shyaway"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfLastMonsterStanding(),
        SetTarget(SELF),
        CastSpell(Escape),
        Wait1TurnandRestartScript(),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        CastSpell(WillyWisp),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack10, PhysicalAttack10, Elegy),
        StartCounterCommands(),
    ]
)
