"""183 - PyrosphereHenchman"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 3),
        CastSpell(Drain, Drain, FlameStone),
        Wait1TurnandRestartScript(),
        Attack(AttackDoNothing, PhysicalAttack2, PhysicalAttack2),
        StartCounterCommands(),
    ]
)
