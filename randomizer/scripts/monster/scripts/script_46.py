"""46 - Cluster"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        CastSpell(Crystal),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack1),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_SPECIAL]),
        Attack(Psyche),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
