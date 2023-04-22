"""235 - Shyper"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        CastSpell(SwordRain),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack13),
        StartCounterCommands(),
        IfHPBelow(0),
        IfVarBitsSet(0x7EE004, [0]),
        ClearVarBits(0x7EE00E, [0]),
        DoMonsterBehaviour(3),
        DecreaseVarBy1(0x7EE000),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfHPBelow(0),
        IfVarBitsSet(0x7EE004, [1]),
        ClearVarBits(0x7EE00E, [1]),
        DoMonsterBehaviour(3),
        DecreaseVarBy1(0x7EE000),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
