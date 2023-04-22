"""110 - Pulsar"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        Attack(PhysicalAttack1),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Wait1TurnandRestartScript(),
        CastSpell(StaticE, Electroshock, Bolt),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_ATTACK]),
        Attack(Migraine),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
