# 238 - Smithy2MageHead

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        CastSpell(SwordRain, SpearRain, ArrowRain),
        Wait1TurnandRestartScript(),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 7),
        CastSpell(MeteorSwarm, Boulder, DarkStar),
        Wait1TurnandRestartScript(),
        CastSpell(Shredder),
        StartCounterCommands(),
        IfHPBelow(0),
        RunBattleEvent(BE0098_SMITHY_IS_DEFEATED),
        ExitBattle(),
        Wait1TurnandRestartScript(),
        IfHPBelow(2000, identifier="mage_threshold_lowest"),
        IfVarBitsClear(0x7EE002, [5]),
        SetVarBits(0x7EE002, [2]),
        SetVarBits(0x7EE002, [5]),
        ClearVarBits(0x7EE002, [1]),
        ClearVar(0x7EE009),
        Wait1TurnandRestartScript(),
        IfHPBelow(4000, identifier="mage_threshold_mid"),
        IfVarBitsClear(0x7EE002, [6]),
        SetVarBits(0x7EE002, [1]),
        SetVarBits(0x7EE002, [6]),
        ClearVarBits(0x7EE002, [0]),
        ClearVar(0x7EE009),
        Wait1TurnandRestartScript(),
        IfHPBelow(6000, identifier="mage_threshold_highest"),
        IfVarBitsClear(0x7EE002, [7]),
        SetVarBits(0x7EE002, [0]),
        SetVarBits(0x7EE002, [7]),
        ClearVar(0x7EE009),
        Wait1TurnandRestartScript(),
    ]
)
