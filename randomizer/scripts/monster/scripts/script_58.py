"""58 - Artichoker"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        CastSpell(StaticE),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack1, PhysicalAttack40, Stench),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_SPECIAL]),
        SetTarget(RANDOM_ALLY_OR_SELF),
        CastSpell(Recover),
        SetTarget(RANDOM_OPPONENT),
        Wait1TurnandRestartScript(),
    ]
)
