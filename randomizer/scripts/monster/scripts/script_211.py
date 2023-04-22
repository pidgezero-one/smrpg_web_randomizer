"""211 - AxemGreen"""

from randomizer.scripts.monster.script_imports import *

script = MonsterScript(
    [
        IfVarBitsSet(0x7EE003, [4]),
        Wait1TurnandRestartScript(),
        ClearVar(DESIGNATED_RANDOM_NUM_VAR),
        Set7EE005ToRandomNumber(upper_bound=7),
        IfVarLessThan(DESIGNATED_RANDOM_NUM_VAR, 6),
        CastSpell(MeteorBlast, Solidify, StaticE),
        Wait1TurnandRestartScript(),
        Attack(PhysicalAttack3, PhysicalAttack3, Elegy),
        StartCounterCommands(),
        IfCurrentlyInFormationID(304),
        IfHPBelow(0),
        IfVarEqualOrGreaterThan(0x7EE00F, 4),
        SetUntargetable(SELF),
        SetTargetable(MONSTER_1_SET),
        SetVarBits(0x7EE003, [4]),
        SetVarBits(0x7EE002, [0]),
        RunBattleEvent(BE0067_AXEM_RANGERS_GROUP_FORMATION),
        Wait1TurnandRestartScript(),
        IfCurrentlyInFormationID(304),
        IfHPBelow(0),
        IncreaseVarBy1(0x7EE00F),
        SetUntargetable(SELF),
        SetVarBits(0x7EE003, [4]),
        RunBattleEvent(BE0066_UNUSED),
        Wait1TurnandRestartScript(),
    ]
)
