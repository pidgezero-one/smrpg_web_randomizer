"""71 - Chewy"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        Attack(PhysicalAttack4),
        Wait1TurnandRestartScript(),
        CastSpell(SpellDoNothing, Drain, MegaDrain),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_ATTACK]),
        Attack(PollenNap),
        Wait1TurnandRestartScript(),
    ]
)
