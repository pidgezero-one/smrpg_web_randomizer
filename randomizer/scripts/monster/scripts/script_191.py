# 191 - LeftEye

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsSet(0x7EE003, [0]),
        IfVarEqualOrGreaterThan(0x7EE004, 2),
        SetTargetable(SELF),
        ClearVar(0x7EE004),
        ClearVar(0x7EE003),
        DoMonsterBehaviour(13),
        Wait1TurnandRestartScript(),
        IfVarBitsSet(0x7EE003, [0]),
        IncreaseVarBy1(0x7EE004),
        Wait1TurnandRestartScript(),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        SetVarBits(0x7EE00F, [0]),
        Attack(PhysicalAttack0, GunkBall, PhysicalAttack0),
        ClearVarBits(0x7EE00F, [0]),
        Wait1TurnandRestartScript(),
        SetVarBits(0x7EE00F, [0]),
        Attack(PhysicalAttack0, VenomDrool, ScrowBell),
        ClearVarBits(0x7EE00F, [0]),
        StartCounterCommands(),
        IfHPBelow(0),
        IfVarBitsClear(0x7EE008, [0]),
        SetVarBits(0x7EE003, [0]),
        SetVarBits(0x7EE000, [1]),
        ClearVarBits(0x7EE000, [2]),
        SetUntargetable(SELF),
        MakeVulnerable(MONSTER_1_SET, identifier="left_eye_revive_exor"),
        DoMonsterBehaviour(12),
        RunBattleDialog(219),
        Wait1TurnandRestartScript(),
    ]
)
