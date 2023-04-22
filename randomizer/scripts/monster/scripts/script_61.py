"""61 - Hippopo"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 3),
        CastSpell(MegaDrain, Blast, FlameStone),
        Wait1TurnandRestartScript(),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 6),
        CastSpell(SandStorm, Solidify, DrainBeam),
        Wait1TurnandRestartScript(),
        Attack(Poison, BodySlam, PhysicalAttack1),
        StartCounterCommands(),
    ]
)
