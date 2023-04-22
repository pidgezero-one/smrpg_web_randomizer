"""182 - Smithy2SafeHead"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        CastSpell(Shredder),
        Wait1TurnandRestartScript(),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        SetTarget(RANDOM_ALLY_OR_SELF),
        CastSpell(Recover, MegaRecover, Recover),
        SetTarget(RANDOM_OPPONENT),
        Wait1TurnandRestartScript(),
        StartCounterCommands(),
        IfHPBelow(0),
        RunBattleEvent(BE0098_SMITHY_IS_DEFEATED),
        ExitBattle(),
        Wait1TurnandRestartScript(),
        IfHPBelow(2000, identifier="chest_threshold_lowest"),
        IfVarBitsClear(0x7EE002, [5]),
        SetVarBits(0x7EE002, [2]),
        SetVarBits(0x7EE002, [5]),
        ClearVarBits(0x7EE002, [1]),
        ClearVar(0x7EE009),
        Wait1TurnandRestartScript(),
        IfHPBelow(4000, identifier="chest_threshold_mid"),
        IfVarBitsClear(0x7EE002, [6]),
        SetVarBits(0x7EE002, [1]),
        SetVarBits(0x7EE002, [6]),
        ClearVarBits(0x7EE002, [0]),
        ClearVar(0x7EE009),
        Wait1TurnandRestartScript(),
        IfHPBelow(6000, identifier="chest_threshold_highest"),
        IfVarBitsClear(0x7EE002, [7]),
        SetVarBits(0x7EE002, [0]),
        SetVarBits(0x7EE002, [7]),
        ClearVar(0x7EE009),
        Wait1TurnandRestartScript(),
    ]
)
