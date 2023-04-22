"""120 - Springer"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        Attack(PhysicalAttack13, PhysicalAttack13, SomnusWaltz),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Wait1TurnandRestartScript(),
        CastSpell(SpellDoNothing, Drain, Drain),
        StartCounterCommands(),
    ]
)
