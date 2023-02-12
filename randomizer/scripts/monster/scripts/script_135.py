# 135 - Shelly

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        StartCounterCommands(),
        IfHPBelow(400, identifier="shelly_hp_phase_1"),
        IfVarBitsClear(0x7EE004, [3]),
        SetVarBits(0x7EE004, [3]),
        DoMonsterBehaviour(4),
        Wait1TurnandRestartScript(),
        IfHPBelow(300, identifier="shelly_hp_phase_2"),
        IfVarBitsClear(0x7EE004, [2]),
        SetVarBits(0x7EE004, [2]),
        DoMonsterBehaviour(5),
        Wait1TurnandRestartScript(),
        IfHPBelow(200, identifier="shelly_hp_phase_3"),
        IfVarBitsClear(0x7EE004, [1]),
        SetVarBits(0x7EE004, [1]),
        DoMonsterBehaviour(6),
        Wait1TurnandRestartScript(),
        IfHPBelow(100, identifier="shelly_hp_phase_4"),
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        DoMonsterBehaviour(7),
        Wait1TurnandRestartScript(),
        IfHPBelow(0),
        DoMonsterBehaviour(8),
        RunBattleEvent(BE0092_SHELLY_BREAKS),
        CallTarget(MONSTER_1_CALL, identifier="shelly_summon"),
        DoMonsterBehaviour(2),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
