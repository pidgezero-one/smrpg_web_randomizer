"""35 - Jawful"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        RunBattleDialog(211),
        Wait1TurnandRestartScript(),
        IfVarBitsSet(0x7EE004, [1]),
        Attack(PhysicalAttack3),
        Wait1TurnandRestartScript(),
        StartCounterCommands(),
        IfTargetedByRegularAttack(),
        IfVarBitsClear(0x7EE004, [2]),
        RunBattleDialog(212),
        SetVarBits(0x7EE004, [1]),
        SetVarBits(0x7EE004, [2]),
        Wait1TurnandRestartScript(),
    ]
)
