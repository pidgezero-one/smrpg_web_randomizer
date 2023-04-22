"""174 - MachineMadeAxemPinkHenchman"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        CastSpell(PetalBlast),
        Wait1TurnandRestartScript(),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        SetTarget(RANDOM_ALLY_OR_SELF),
        CastSpell(Recover, Recover, MegaRecover),
        SetTarget(RANDOM_OPPONENT),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack3, PhysicalAttack3, PhysicalAttack51),
        StartCounterCommands(),
    ]
)
