"""245 - AxemRangers"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        RunBattleEvent(BE0062_UNUSED),
        SetUntargetable(SELF),
        Wait1TurnandRestartScript(),
        IfVarBitsClear(0x7EE004, [1]),
        IfVarBitsSet(0x7EE002, [0]),
        SetVarBits(0x7EE004, [1]),
        RunBattleDialog(180),
        RunBattleDialog(181),
        CastSpell(BreakerBeam),
        Wait1TurnandRestartScript(),
        IfVarBitsSet(0x7EE002, [0]),
        IfVarEqualOrGreaterThan(0x7EE00D, 1),
        ClearVar(0x7EE00D),
        CastSpell(BreakerBeam),
        Wait1TurnandRestartScript(),
        IfVarBitsSet(0x7EE002, [0]),
        RunBattleDialog(222),
        IncreaseVarBy1(0x7EE00D),
        Wait1TurnandRestartScript(),
        StartCounterCommands(),
        IfHPBelow(0),
        RunBattleEvent(BE0069_AXEM_RANGERS_ARE_DEFEATED),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
