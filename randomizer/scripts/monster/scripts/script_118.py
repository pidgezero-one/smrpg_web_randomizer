"""118 - FinkFlower"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 6),
        SetVarBits(0x7EE00F, [0]),
        Attack(PhysicalAttack4, ScrowDust, PollenNap),
        ClearVarBits(0x7EE00F, [0]),
        Wait1TurnandRestartScript(),
        SetTarget(RANDOM_ALLY_OR_SELF),
        CastSpell(Recover, Recover, SpellDoNothing),
        SetTarget(RANDOM_OPPONENT),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_ATTACK]),
        SetVarBits(0x7EE00F, [0]),
        Attack(PhysicalAttack4, AttackDoNothing, AttackDoNothing),
        ClearVarBits(0x7EE00F, [0]),
        Wait1TurnandRestartScript(),
    ]
)
