"""203 - Thrax"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        SetUntargetable(SELF),
        Wait1TurnandRestartScript(),
        StartCounterCommands(),
    ]
)
