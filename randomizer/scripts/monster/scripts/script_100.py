"""100 - Gorgon"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 2),
        Attack(PhysicalAttack1, PhysicalAttack1, Echofinder),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Wait1TurnandRestartScript(),
        CastSpell(WillyWisp, WillyWisp, DiamondSaw),
        StartCounterCommands(),
    ]
)
