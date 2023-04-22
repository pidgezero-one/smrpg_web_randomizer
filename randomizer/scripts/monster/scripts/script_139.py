"""139 - Chester"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        DoMonsterBehaviour(7),
        CallTarget(MONSTER_2_CALL),
        RunBattleDialog(216),
        Wait1TurnandRestartScript(),
        IfVarBitsClear(0x7EE004, [0]),
        CastSpell(FlameStone),
        SetVarBits(0x7EE004, [0]),
        Wait1TurnandRestartScript(),
        CastSpell(SandStorm),
        Wait1Turn(),
        CastSpell(MegaRecover, MegaRecover, FlameWall),
        Wait1Turn(),
        StartCounterCommands(),
    ]
)
