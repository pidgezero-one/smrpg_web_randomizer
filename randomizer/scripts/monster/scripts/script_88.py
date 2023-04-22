"""88 - SlingShy"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfLastMonsterStanding(),
        SetTarget(SELF),
        CastSpell(Escape),
        Wait1TurnandRestartScript(),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 5),
        Attack(PhysicalAttack107),
        Wait1TurnandRestartScript(),
        Attack(ScrowBell, DoomReverb, SporeChimes),
        StartCounterCommands(),
        IfTargetedByCommand([COMMAND_ATTACK]),
        Attack(PhysicalAttack107, AttackDoNothing, AttackDoNothing),
        Wait1TurnandRestartScript(),
    ]
)
