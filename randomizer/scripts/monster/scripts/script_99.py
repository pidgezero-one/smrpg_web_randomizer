"""99 - Forkies"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        RunBattleDialog(152),
        Wait1TurnandRestartScript(),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarBitsSet(0x7EE004, [1]),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        CastSpell(Storm),
        Wait1TurnandRestartScript(),
        IfVarBitsSet(0x7EE004, [1]),
        Attack(PhysicalAttack3),
        Wait1TurnandRestartScript(),
        StartCounterCommands(),
        IfTargetedByRegularAttack(),
        IfVarBitsClear(0x7EE004, [2]),
        RunBattleDialog(153),
        SetVarBits(0x7EE004, [1]),
        SetVarBits(0x7EE004, [2]),
        Wait1TurnandRestartScript(),
    ]
)
