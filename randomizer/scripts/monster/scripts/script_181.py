# 181 - Smithy2TankHead

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        Attack(PhysicalAttack81, PhysicalAttack81, Magnum),
        Wait1Turn(),
        Attack(PhysicalAttack81),
        StartCounterCommands(),
        IfHPBelow(0),
        RunBattleEvent(BE0098_SMITHY_IS_DEFEATED),
        ExitBattle(),
        Wait1TurnandRestartScript(),
        IfHPBelow(2000, identifier="tank_threshold_lowest"),
        IfVarBitsClear(0x7EE002, [5]),
        SetVarBits(0x7EE002, [2]),
        SetVarBits(0x7EE002, [5]),
        ClearVarBits(0x7EE002, [1]),
        ClearVar(0x7EE009),
        Wait1TurnandRestartScript(),
        IfHPBelow(4000, identifier="tank_threshold_half"),
        IfVarBitsClear(0x7EE002, [6]),
        SetVarBits(0x7EE002, [1]),
        SetVarBits(0x7EE002, [6]),
        ClearVarBits(0x7EE002, [0]),
        ClearVar(0x7EE009),
        Wait1TurnandRestartScript(),
        IfHPBelow(6000, identifier="tank_threshold_highest"),
        IfVarBitsClear(0x7EE002, [7]),
        SetVarBits(0x7EE002, [0]),
        SetVarBits(0x7EE002, [7]),
        ClearVar(0x7EE009),
        Wait1TurnandRestartScript(),
    ]
)
