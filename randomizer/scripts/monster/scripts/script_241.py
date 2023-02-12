# 241 - Croco2

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsSet(0x7EE004, [1]),
        Attack(PhysicalAttack14, Chomp, Chomp),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack14, PhysicalAttack25, PhysicalAttack25),
        StartCounterCommands(),
        IfVarBitsClear(0x7EE004, [0]),
        IfHPBelow(400, identifier="croco2_item_steal"),
        SetVarBits(0x7EE004, [0, 1]),
        RunBattleEvent(BE0015_CROCO_STEALS_ITEMS_YOU_WANT_THEM_BACK),
        RemoveAllInventory(),
        ClearVar(0x7EE00F),
        Wait1TurnandRestartScript(),
        IfHPBelow(0),
        RunBattleEvent(BE0016_CROCO_RETURNS_ITEMS_ENOUGH_HERE_S_YOUR_JUNK),
        RestoreInventory(),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
