"""31 - Wiggler"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        Attack(PhysicalAttack1, PhysicalAttack40, PhysicalAttack1),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Wait1TurnandRestartScript(),
        CastSpell(SandStorm, SandStorm, SpellDoNothing),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_ATTACK]),
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        SetTarget(SELF),
        Attack(Vigorup),
        SetTarget(RANDOM_OPPONENT),
        Wait1TurnandRestartScript(),
    ]
)
