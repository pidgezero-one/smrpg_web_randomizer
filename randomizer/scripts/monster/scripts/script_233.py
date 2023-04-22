"""233 - Exor"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsClear(0x7EE000, [0, 1, 2]),
        IfTargetAlive(MONSTER_3_SET),
        IfTargetAlive(MONSTER_4_SET),
        SetVarBits(0x7EE000, [2]),
        RunBattleDialog(218),
        MakeInvulnerable(MONSTER_1_SET, identifier="protect_exor"),
        Wait1TurnandRestartScript(),
        StartCounterCommands(),
        IfHPBelow(0),
        SetVarBits(0x7EE008, [0]),
        SetUntargetable(MONSTER_2_SET),
        SetUntargetable(MONSTER_3_SET),
        SetUntargetable(MONSTER_4_SET),
        RunBattleEvent(BE0081_EXOR_IS_DEFEATED_CRIES_AND_OPENS_MOUTH),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
    ]
)
