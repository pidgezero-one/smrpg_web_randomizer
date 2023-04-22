"""56 - Dodo"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsSet(0x7EE003, [3]),
        Wait1TurnandRestartScript(),
        IfVarBitsClear(0x7EE003, [1]),
        Attack(PhysicalAttack1, Multistrike, FlutterHush),
        Wait1TurnandRestartScript(),
        IfVarBitsSet(0x7EE003, [2]),
        Attack(PhysicalAttack1, Multistrike, FlutterHush),
        Wait1TurnandRestartScript(),
        StartCounterCommands(),
        IfHPBelow(600, identifier="dodo_solo_ends"),
        IfVarBitsSet(0x7EE003, [6]),
        IfVarBitsClear(0x7EE003, [3]),
        IfVarBitsClear(0x7EE003, [5]),
        SetVarBits(0x7EE003, [5]),
        SetVarBits(0x7EE003, [3]),
        SetVarBits(0x7EE003, [1]),
        SetUntargetable(SELF),
        SetTargetable(MONSTER_1_SET),
        RunBattleEvent(BE0049_DODO_FLUTTERS_AND_LEAVES_BATTLE),
        Wait1TurnandRestartScript(),
        IfHPBelow(0),
        SetVarBits(0x7EE003, [3]),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfTargetedByRegularAttack(),
        Attack(PhysicalAttack1, AttackDoNothing, AttackDoNothing),
        Wait1TurnandRestartScript(),
    ]
)
