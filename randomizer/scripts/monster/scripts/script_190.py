"""190 - RightEye"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsSet(0x7EE002, [0]),
        IfVarEqualOrGreaterThan(0x7EE004, 3),
        SetTargetable(SELF),
        ClearVar(0x7EE004),
        ClearVar(0x7EE002),
        DoMonsterBehaviour(13),
        Wait1TurnandRestartScript(),
        IfVarBitsSet(0x7EE002, [0]),
        IncreaseVarBy1(0x7EE004),
        Wait1TurnandRestartScript(),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 4),
        CastSpell(Bolt, DiamondSaw, MegaDrain),
        Wait1TurnandRestartScript(),
        CastSpell(FlameStone, DarkStar, Blast),
        StartCounterCommands(),
        IfHPBelow(0),
        IfVarBitsClear(0x7EE008, [0]),
        SetVarBits(0x7EE002, [0]),
        SetVarBits(0x7EE000, [0]),
        ClearVarBits(0x7EE000, [2]),
        SetUntargetable(SELF),
        MakeVulnerable(MONSTER_1_SET, identifier="right_eye_revive_exor"),
        DoMonsterBehaviour(11),
        RunBattleDialog(219),
        Wait1TurnandRestartScript(),
    ]
)
