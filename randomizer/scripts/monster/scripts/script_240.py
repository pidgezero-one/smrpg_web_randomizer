"""240 - Croco1"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsSet(0x7EE003, [0]),
        ClearVarBits(0x7EE003, [0]),
        RunBattleDialog(131),
        Wait1TurnandRestartScript(),
        IfHPBelow(100, identifier="croco_heal_threshold"),
        IfVarBitsClear(0x7EE004, [0]),
        SetVarBits(0x7EE004, [0]),
        SetTarget(SELF),
        CastSpell(WeirdMushroom),
        SetTarget(RANDOM_OPPONENT),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack14, PhysicalAttack14, PhysicalAttack25),
        StartCounterCommands(),
        IfHPBelow(0),
        DoMonsterBehaviour(3),
        RemoveTarget(SELF),
        Wait1TurnandRestartScript(),
        IfVarBitsClear(0x7EE003, [0, 1]),
        IfTargetedByElement([Element.FIRE]),
        SetVarBits(0x7EE003, [0, 1]),
        RunBattleDialog(1),
        Wait1TurnandRestartScript(),
    ]
)
